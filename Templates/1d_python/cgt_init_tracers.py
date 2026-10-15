def cgt_init_tracers():
    #--------------------------------
    # load initial values for tracers
    #--------------------------------

    # some need to be loaded from files
<tracers vertLoc=WAT; useInitValue=0>
    global tracer_vector_<name>
    tracer_vector_<name> = np.loadtxt('init/<trimName>.txt')

</tracers>
<tracers vertLoc=SED; useInitValue=0>
    global tracer_scalar_<name>
    tracer_scalar_<name> = float(np.loadtxt('init/<trimName>.txt'))

</tracers>
<tracers vertLoc=SUR; useInitValue=0>
    global tracer_scalar_<name>
    tracer_scalar_<name> = float(np.loadtxt('init/<trimName>.txt'))

</tracers>

    # others are initialized as constant
<tracers vertLoc=WAT; useInitValue=1>
    global tracer_vector_<name>
    tracer_vector_<name> = np.full(kmax,<initValue>)
</tracers>
<tracers vertLoc=SED; useInitValue=1>
    global tracer_scalar_<name>
    tracer_scalar_<name> = <initValue>
</tracers>
<tracers vertLoc=SUR; useInitValue=1>
    global tracer_scalar_<name>
    tracer_scalar_<name> = <initValue>
</tracers>

    # some tracers have vertical movement
<tracers vertLoc=WAT; vertSpeed/=0>
    global vertical_speed_of_<name>
    vertical_speed_of_<name> = np.zeros(kmax)
    global vertical_diffusivity_of_<name>
    vertical_diffusivity_of_<name> = np.zeros(kmax)
</tracers>

    # auxiliaries which communicate data from the last time step are set to 0
<auxiliaries vertLoc=WAT; isUsedElsewhere=1>
    global auxiliary_vector_<name>
    auxiliary_vector_<name> = np.zeros(kmax)
</auxiliaries>
<auxiliaries vertLoc=SED; isUsedElsewhere=1>
    global auxiliary_scalar_<name>
    auxiliary_scalar_<name> = 0.0;
</auxiliaries>
<auxiliaries vertLoc=SUR; isUsedElsewhere=1>
    global auxiliary_scalar_<name>
    auxiliary_scalar_<name> = 0.0;
</auxiliaries>
