The main changes to ERGOM here are related to photo-acclimation, so that the optimal light level varies depending upon surface irradiance,
near-surface optical depth, near-surface vertical diffusivity, and the photo-acclimation timescale of phytoplankton.  The last is added
as a constant which can be chosen prior to running the model.

These modifications build on results from Lagrangian modelling: https://github.com/atwelves/phyto_gedanken/tree/master 

## Photo-acclimation ##

By default, ERGOM calculates light limitation based on the discrepancy between ambient light and the (constant) optimal light for each plankton group.  In reality, plankton light systems adapt to the light they are exposed to, so that the instatantaneous light limitation depends also on the light that the plankton have been exposed to over the preceding hours.  This can be accounted for in a biogeochemical model by allowing the optimal light to evolve dynamically as conditions change.  

The light which a phytoplankton bloom is exposed to on average can be estimated by considering the evolution of the light level when averaged over the mixed layer depth D.  This evolution will be a function both of changes to the surface irradiance I_0 and changes to the underwater environment (D itself, plus the attenuation coefficient k_ext

I_mld = 
