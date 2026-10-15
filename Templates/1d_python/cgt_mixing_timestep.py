def cgt_mixing_timestep():
  <tracers vertLoc=WAT>
    global tracer_vector_<name>
  </tracers>
    global forcing_vector_diffusivity
    # vertical diffusion of all tracers
    forcing_vector_diffusivity = np.fmax(forcing_vector_diffusivity, min_diffusivity)
    forcing_vector_diffusivity = np.fmin(forcing_vector_diffusivity, max_diffusivity)
    for m in range(num_vdiff_steps):
      # second, diffuse the tracers (including marked tracers) themselves
      <tracers vertLoc=WAT>
        tracer_vector_<name> = vdiff_explicit(forcing_vector_diffusivity, 
                               tracer_vector_<name>, 
                               tracer_vector_<name>, tracer_vector_<name>, 
                                cellheights, timestep/num_vdiff_steps*(24*3600))
      </tracers>