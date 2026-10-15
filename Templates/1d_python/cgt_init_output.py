def cgt_init_output():
    #-----------------------------
    # initialize the output arrays
    #-----------------------------
    import numpy as np
    # auxiliary variables
<auxiliaries vertLoc=WAT; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = np.full((max_output_index,kmax),np.nan)
    global output_vector_<name>
    output_vector_<name> = np.zeros(kmax)
</auxiliaries>
<auxiliaries vertLoc=SED; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = [np.nan for l in range(max_output_index)]
    global output_scalar_<name>
    output_scalar_<name> = 0.0
</auxiliaries>
<auxiliaries vertLoc=SUR; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = [np.nan for l in range(max_output_index)]
    global output_scalar_<name>
    output_scalar_<name> = 0.0
</auxiliaries>

    # tracers
<tracers vertLoc=WAT; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = np.full((max_output_index,kmax),np.nan)
    global output_vector_<name>
    output_vector_<name> = [0 for k in range(kmax)]
</tracers>
<tracers vertLoc=SED; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = [np.nan for l in range(max_output_index)]
    global output_scalar_<name>
    output_scalar_<name> = 0.0
</tracers>
<tracers vertLoc=SUR; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = [np.nan for l in range(max_output_index)]
    global output_scalar_<name>
    output_scalar_<name> = 0.0
</tracers>

    # processes
<processes vertLoc=WAT; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = np.full((max_output_index,kmax),np.nan)
    global output_vector_<name>
    output_vector_<name> = [0 for k in range(kmax)]
</processes>
<processes vertLoc=SED; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = [np.nan for l in range(max_output_index)]
    global output_scalar_<name>
    output_scalar_<name> = 0.0
</processes>
<processes vertLoc=SUR; isOutput=1>
    # <description> :
    global output_<name>
    output_<name> = [np.nan for l in range(max_output_index)]
    global output_scalar_<name>
    output_scalar_<name> = 0.0
</processes>