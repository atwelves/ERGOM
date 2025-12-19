**Contents**

- ERGOM text files in *Textfiles_IOW/*,modified to include photo-acclimation 
- A modified coupling of the NEMO-TOP module to FABM in MY_SRC/trcsms_fabm.F90, allowing NEMO to pass mixed layer depth and surface diffusivity to FABM
- A modified ERGOM code template for FABM, including the new FABM variables: mixed layer depth, surface diffusivity and surface attenuation coefficient
- A version of the GOTM light module light.F90, modified to pass surface attenuation coefficient to FABM
- A fabm.yaml file including the new constant $\tau_{acc}$
- A variables.yaml file now including all the new FABM variables
- A version of namelist_top_ref designed to run with the Gulf of Finland setup

The main changes to ERGOM here are related to photo-acclimation, so that the optimal light level varies depending upon surface irradiance,
near-surface optical depth, near-surface vertical diffusivity, and the photo-acclimation timescale of phytoplankton.  The last is added
as a constant which can be chosen prior to running the model.

These modifications build on results from Lagrangian modelling: https://github.com/atwelves/phyto_gedanken/tree/master 

## Photo-acclimation ##

By default, ERGOM calculates light limitation based on the discrepancy between ambient light and the (constant) optimal light for each plankton group.  In reality, plankton light systems adapt to the light they are exposed to, so that the instatantaneous light limitation depends also on the light that the plankton have been exposed to over the preceding hours.  This can be accounted for in a biogeochemical model by allowing the optimal light to evolve dynamically as conditions change.  

The light which a phytoplankton bloom is exposed to on average can be estimated by considering the evolution of the light level when averaged over the mixed layer depth D.  This evolution will be a function both of changes to the surface irradiance I_0 and changes to the underwater environment (D itself, plus the attenuation coefficient k

$$I_{mld} = \frac{I_{0}}{\kappa D}(1-e^{-\kappa D})$$

At the same time, the light to which individual phytoplankton cells are exposed to will vary as they are transported around the mixed layer, with a characteristic timescale

$$\tau_{mix} = \frac{D^{2}}{K_{z}}$$

Here we concentrate only on the impact that mixing has on light exposure, thus neglecting changes to bulk properties of the mixed layer and to the surface irradiance.  We define the ratio of mixing timescale to the acclimation timescale as 

$$\zeta = \frac{\tau_{mix}}{\tau_{acc}} = \frac{D^{2}}{K_{z}\tau_{acc}}$$

Then we hypothesize that the light exposure over timescale $\tau_{acc}$ is 

$$I_{mem} - I_{mld} = \frac{\zeta}{\zeta + R} (I_{mem} - I_{mld})$$

and we use Lagrangian simulations (https://github.com/atwelves/phyto_gedanken/tree/master) over a range of $D$, $\tau_{acc}$ and $K_{z}$ to determine that $R \approx 10$ under constant surface irradiance.

Then we assume that the irradiance memory modifies the optimal light level according to 

$$I_{opt} = \frac{I_{opt}^{0}}{2} + \frac{I_{mem}}{2}$$

We implement this system of equations into ERGOM, which requires some simplifications: we use only the surface diffusivity and surface attenuation coefficient etc. etc., 
