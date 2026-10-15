def cgt_calc_opacity_bio():
    global forcing_vector_opacity_bio
    #-----------------------------------------------------------------
    # fill the vector opacity_bio with the opacity caused by POM [1/m]
    #-----------------------------------------------------------------
    forcing_vector_opacity_bio = np.zeros(kmax)
    
    # water column tracers
    # calculate opacity contribution [1/m] as product of
    # opacity [m2/mol] * concentration [mol/kg] * water density [kg/m3]
    for k in range(kmax):
        forcing_vector_opacity_bio[k] = forcing_vector_opacity_bio[k] + \
      <tracers vertLoc=WAT; opacity/=0>
        <opacity> * tracer_vector_<name>[k] * density_water + \
      </tracers>
        0.0
    
    # surface tracers (only in uppermost cell)
    # calculate opacity contribution [1/m] as product of
    # opacity [m2/mol] * concentration [mol/m2] / cell height [m]
    forcing_vector_opacity_bio[0] = forcing_vector_opacity_bio[0] + \
    <tracers vertLoc=SUR; opacity/=0>
    <opacity> * tracer_scalar_<name> / depths[0] + \
    </tracers>
    0.0