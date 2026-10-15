def theta(x):
    if x>0:
        return(1.0)
    else:
        return(0.0)

def exp(x):
    import math
    return math.exp(x)

def log(x):
    import math
    return math.log(x)

def sqrt(x):
    import math
    return math.sqrt(x)

def power(base, exponent):
    return base ** exponent

def cgt_bio_timestep(): 
    import numpy as np
    # declare which global variables we want to modify
  <tracers vertLoc=WAT>
    global tracer_vector_<name>
  </tracers>
  <tracers vertLoc=SED>
    global tracer_scalar_<name>
  </tracers>
  <tracers vertLoc=WAT; isOutput=1>
    global output_vector_<name>
  </tracers>
  <tracers vertLoc=SED; isOutput=1>
    global output_scalar_<name>
  </tracers>
  <tracers vertLoc=WAT; vertSpeed/=0>
    global vertical_speed_of_<name>
    global vertical_diffusivity_of_<name>
  </tracers>      
  <auxiliaries vertLoc=WAT; isOutput=1>             
    global output_vector_<name>
  </auxiliaries>
  <auxiliaries vertLoc=SED; isOutput=1>
    global output_scalar_<name>
  </auxiliaries>
  <auxiliaries vertLoc=SUR; isOutput=1>
    global output_scalar_<name>
  </auxiliaries>
  <auxiliaries vertLoc=WAT; isUsedElsewhere=1>             
    global auxiliary_vector_<name>
  </auxiliaries>
  <auxiliaries vertLoc=SED; isUsedElsewhere=1>             
    global auxiliary_scalar_<name>
  </auxiliaries>
  <auxiliaries vertLoc=SUR; isUsedElsewhere=1>             
    global auxiliary_scalar_<name>
  </auxiliaries>
  <processes vertLoc=WAT; isOutput=1>
    global output_vector_<name>
  </processes>
  <processes vertLoc=SED; isOutput=1>
    global output_scalar_<name>
  </processes>            
  <processes vertLoc=SUR; isOutput=1>
    global output_scalar_<name>
  </processes>          
  <celements>
    global tracer_vector_<total>
    global tracer_scalar_<totalBottom>
  </celements>
  
    # calculate total element concentrations in the water column
  <celements>
    tracer_vector_<total> = np.zeros(kmax)
  </celements>  
    for k in range(kmax):
        cgt_dummyvar = 0.0
      <celements>
        tracer_vector_<total>[k] = (
          <containingTracers vertLoc=WAT>
                max(0.0,tracer_vector_<ct>[k])*<ctAmount> + 
          </containingTracers>
                0.0 )
      </celements>   
     

    # calculate total colored element concentrations at bottom
  <celements>
    tracer_scalar_<totalBottom> = (
      <containingTracers vertLoc=SED>
         max(0.0,tracer_scalar_<ct>)*<ctAmount> + 
      </containingTracers>
         0.0 )
  </celements>    

    # Water column processes

    cgt_bottomdepth = 0.0 
    for k in range(kmax):
            cgt_bottomdepth = cgt_bottomdepth + cellheights[k]
          
            #------------------------------------
            # STEP 1: prepare abiotic parameters
            #------------------------------------
            cgt_temp       = forcing_vector_temperature[k]             # potential temperature     [Celsius]
            cgt_sali       = forcing_vector_salinity[k]                # salinity                  [g/kg]
            cgt_diffusivity= forcing_vector_diffusivity[k]             # diffusivity               [m2/s]
            cgt_light      = forcing_vector_light[k]                   # light intensity           [W/m2]
            cgt_cellheight = cellheights[k]                            # cell height               [m]
            cgt_density    = density_water                             # density                   [kg/m3]
            cgt_timestep   = timestep                                  # timestep                  [days]
            cgt_longitude  = location_longitude                        # geographic longitude      [deg]
            cgt_latitude   = location_latitude                         # geographic latitude       [deg]
            cgt_dTdz       = dTdZ[k]                               # detrital sinking speed scaling factor []
            if (k == kmax-1):
                cgt_current_wave_stress=forcing_scalar_bottom_stress    # bottom stress             [N/m2]
                                   
             
            #------------------------------------
            # STEP 2: load tracer values
            #------------------------------------
          <tracers vertLoc=WAT>
            <name> = float(tracer_vector_<name>[k])   # <description>
            if (k == 0):
                above_<name> = float(tracer_vector_<name>[k]) 
            else:
               above_<name> = float(tracer_vector_<name>[k-1])
             
          </tracers>             
          <auxiliaries vertLoc=WAT; isUsedElsewhere=1>
            <name> = float(auxiliary_vector_<name>[k])   # <description>
          </auxiliaries>

          <tracers vertLoc=WAT; isPositive=1>
            <name>       = max(<name>,0.0) 
            above_<name> = max(above_<name>,0.0) 
          </tracers>

            if (k == kmax-1):
                cgt_dummyvar = 0.0
              <tracers vertLoc=SED>
                <name> = tracer_scalar_<name>   # <description>
              </tracers>

              <tracers vertLoc=SED; isPositive=1>
                <name> = max(<name>,0.0) 
              </tracers>
              

            #------------------------------------
            # STEP 4.1: calculate auxiliaries
            #------------------------------------
          <auxiliaries vertLoc=WAT; calcAfterProcesses=0; isZGradient=1>
            # <description> :
            <name> = (above_<formula>-<formula>)/depths[k]
          </auxiliaries>
            # Iterative loops
            #----------------
            # initialize iterative auxiliary variables
          <auxiliaries calcAfterProcesses=0; isZGradient=0; iterations/=0>
            <name> = <iterInit>
          </auxiliaries>  
            
            # iterative loop vertLoc=WAT
            for cgt_iteration in range(1,<maxIterations>+1):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=WAT; calcAfterProcesses=0; isZGradient=0; iterations/=0>
                if cgt_iteration <= <iterations>:
                    # <description> :
                    temp1  = <temp1> 
                    temp2  = <temp2> 
                    temp3  = <temp3> 
                    temp4  = <temp4> 
                    temp5  = <temp5> 
                    temp6  = <temp6> 
                    temp7  = <temp7> 
                    temp8  = <temp8> 
                    temp9  = <temp9> 
                    <name> = <formula>        
              </auxiliaries>

            # iterative loop vertLoc=SED
            if (k == kmax-1):
                for cgt_iteration in range(1,<maxIterations>+1):
                    cgt_dummyvar = 0.0
                  <auxiliaries vertLoc=SED; calcAfterProcesses=0; isZGradient=0; iterations/=0>
                    if cgt_iteration <= <iterations>:
                        # <description> :
                        temp1  = <temp1> 
                        temp2  = <temp2> 
                        temp3  = <temp3> 
                        temp4  = <temp4> 
                        temp5  = <temp5> 
                        temp6  = <temp6> 
                        temp7  = <temp7> 
                        temp8  = <temp8> 
                        temp9  = <temp9> 
                        <name> = <formula>        
                  </auxiliaries>            

            # iterative loop vertLoc=SUR
            if (k == 0):
                for cgt_iteration in range(1,<maxIterations>+1):
                    cgt_dummyvar = 0.0
                  <auxiliaries vertLoc=SUR; calcAfterProcesses=0; isZGradient=0; iterations/=0>
                    if cgt_iteration <= <iterations>:
                        # <description> :
                        temp1  = <temp1> 
                        temp2  = <temp2> 
                        temp3  = <temp3> 
                        temp4  = <temp4> 
                        temp5  = <temp5> 
                        temp6  = <temp6> 
                        temp7  = <temp7> 
                        temp8  = <temp8> 
                        temp9  = <temp9> 
                        <name> = <formula>        
                  </auxiliaries>            


            # Normal, non-iterative auxiliary variables
            #------------------------------------------
          <auxiliaries vertLoc=WAT; calcAfterProcesses=0; isZGradient=0; iterations=0>
            # <description> :
            temp1  = <temp1> 
            temp2  = <temp2> 
            temp3  = <temp3> 
            temp4  = <temp4> 
            temp5  = <temp5> 
            temp6  = <temp6> 
            temp7  = <temp7> 
            temp8  = <temp8> 
            temp9  = <temp9> 
            <name> = <formula> 
             
          </auxiliaries>

            if (k == kmax-1):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SED; calcAfterProcesses=0; iterations=0>
                # <description> :
                temp1  = <temp1> 
                temp2  = <temp2> 
                temp3  = <temp3> 
                temp4  = <temp4> 
                temp5  = <temp5> 
                temp6  = <temp6> 
                temp7  = <temp7> 
                temp8  = <temp8> 
                temp9  = <temp9> 
                <name> = <formula>  
                
              </auxiliaries>
              
             
            if (k == 0):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SUR; calcAfterProcesses=0; iterations=0>
                # <description> :
                temp1  = <temp1> 
                temp2  = <temp2> 
                temp3  = <temp3> 
                temp4  = <temp4> 
                temp5  = <temp5> 
                temp6  = <temp6> 
                temp7  = <temp7> 
                temp8  = <temp8> 
                temp9  = <temp9>                 
                <name> = <formula>  
                
              </auxiliaries>
              
             
            #------------------------------------
            # STEP 4.2: output of auxiliaries
            #------------------------------------
          <auxiliaries vertLoc=WAT; calcAfterProcesses=0; isOutput=1>             
            output_vector_<name>[k] = output_vector_<name>[k] + <name> 
          </auxiliaries>

            if (k == kmax-1):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SED; calcAfterProcesses=0; isOutput=1>
                output_scalar_<name> = output_scalar_<name> + <name> 
              </auxiliaries>
              
            if (k == 0):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SUR; calcAfterProcesses=0; isOutput=1>
                output_scalar_<name> = output_scalar_<name> + <name> 
              </auxiliaries>
              

            #------------------------------------
            # STEP 5: calculate process limitations
            #------------------------------------

          <tracers vertLoc=WAT>
           <limitations>
            <name> = <formula> 
           </limitations>
          </tracers>

            if (k == kmax-1):
                cgt_dummyvar = 0.0
              <tracers vertLoc=SED>
               <limitations>
                <name> = <formula> 
               </limitations>
              </tracers>
              

            if (k == 0):
                cgt_dummyvar = 0.0
              <tracers vertLoc=SUR>
               <limitations>
                <name> = <formula> 
               </limitations>
              </tracers>
              

            #------------------------------------
            #-- POSITIVE-DEFINITE SCHEME --------
            #-- means the following steps will be repeated as often as nessecary
            #------------------------------------

            fraction_of_total_timestep = 1.0     # how much of the original timestep is remaining
          <processes>
            total_rate_<name>          = 0.0 
          </processes>
            number_of_loop = 1 

            while (cgt_timestep > 0.0):

                #------------------------------------
                # STEP 6.1: calculate process rates
                #------------------------------------
              <processes vertLoc=WAT>
                # <description> :
                <name> = <turnover> 
                <name> = max(<name>,0.0) 

              </processes>

                if (k == kmax-1):
                    cgt_dummyvar = 0.0
                  <processes vertLoc=SED>
                    # <description> :
                    <name> = <turnover> 
                    <name> = max(<name>,0.0) 
                
                  </processes>
                 
             
                if (k == 0):
                    cgt_dummyvar = 0.0
                  <processes vertLoc=SUR>
                    # <description> :
                    <name> = <turnover> 
                    <name> = max(<name>,0.0) 
                
                  </processes>
                 

                #------------------------------------
                # STEP 6.2: calculate possible euler-forward change (in a full timestep)
                #------------------------------------

              <tracers>
                change_of_<name> = 0.0 
              </tracers>

              <tracers vertLoc=WAT; hasRatesFlat=0>
             
                change_of_<name> = change_of_<name> + cgt_timestep*(0.0 
                  <timeTendencies vertLoc=WAT>
                    <timeTendency>   # <description>
                  </timeTendencies>
                ) 
              </tracers>

                if (k == 0):
                    cgt_dummyvar = 0.0
                  <tracers vertLoc=WAT; hasRatesFlat=2>

                    change_of_<name> = change_of_<name> + cgt_timestep*(0.0 
                      <timeTendencies vertLoc=SUR>
                        <timeTendency>   # <description>
                      </timeTendencies>
                    ) 
                  </tracers>
                 

                if (k == kmax-1):
                    cgt_dummyvar = 0.0
                  <tracers vertLoc=WAT; hasRatesFlat=1>

                    change_of_<name> = change_of_<name> + cgt_timestep*(0.0 
                      <timeTendencies vertLoc=SED>
                        <timeTendency>   # <description>
                      </timeTendencies>
                    ) 
                  </tracers>
                  <tracers vertLoc=SED; hasRates>

                    change_of_<name> = change_of_<name> + cgt_timestep*(0.0 
                      <timeTendencies>
                        <timeTendency>   # <description>
                      </timeTendencies>
                    ) 
                  </tracers>                         
                            

                #------------------------------------
                # STEP 6.3: calculate maximum fraction of the timestep before some tracer gets exhausted
                #------------------------------------

                timestep_fraction = 1.0 
                which_tracer_exhausted = -1 

                # find the tracer which is exhausted after the shortest period of time

                # in the water column
             <tracers vertLoc=WAT; isPositive=1>
             
                # check if tracer <name> was exhausted from the beginning and is still consumed
                if ((tracer_vector_<name>[k] <= 0.0) & (change_of_<name> < 0.0)):
                    timestep_fraction = 0.0 
                    which_tracer_exhausted = <numTracer> 
                 
                # check if tracer <name> was present, but got exhausted
                if ((tracer_vector_<name>[k] > 0.0) & (tracer_vector_<name>[k] + change_of_<name> < 0.0)):
                    timestep_fraction_new = tracer_vector_<name>[k] / (0.0 - change_of_<name>) 
                    if (timestep_fraction_new <= timestep_fraction):
                        which_tracer_exhausted = <numTracer> 
                        timestep_fraction = timestep_fraction_new 
                    
                 
              </tracers>
          
                # in the bottom layer
                if (k == kmax-1):
                    cgt_dummyvar = 0.0
                  <tracers vertLoc=SED; isPositive=1>

                    # check if tracer <name> was exhausted from the beginning and is still consumed
                    if ((tracer_scalar_<name> <= 0.0) & (change_of_<name> < 0.0)):
                        timestep_fraction = 0.0 
                        which_tracer_exhausted = <numTracer> 
                   
                    # check if tracer <name> was present, but got exhausted
                    if ((tracer_scalar_<name> > 0.0) & (tracer_scalar_<name> + change_of_<name> < 0.0)):
                        timestep_fraction_new = tracer_scalar_<name> / (0.0 - change_of_<name>) 
                        if (timestep_fraction_new <= timestep_fraction):
                            which_tracer_exhausted = <numTracer> 
                            timestep_fraction = timestep_fraction_new 
                       
                    
                  </tracers>                         
                           

                # now, update the limitations: rates of the processes limited by this tracer become zero in the future

              <tracers isPositive=1>
                if (<numTracer> == which_tracer_exhausted):
                    cgt_dummyvar = 0.0
                  <limitations>
                    <name> = 0.0 
                  </limitations>
                 
              </tracers>

                #------------------------------------
                # STEP 6.4: apply a Euler-forward timestep with the fraction of the time
                #------------------------------------ 

                # in the water column
              <tracers vertLoc=WAT>
             
                # tracer <name> (<description>):
                tracer_vector_<name>[k] = tracer_vector_<name>[k] + change_of_<name> * timestep_fraction 
              </tracers>
          
                # in the bottom layer
                if (k == kmax-1):
                    cgt_dummyvar = 0.0
              <tracers vertLoc=SED>

                    # tracer <name> (<description>)
                    tracer_scalar_<name> = tracer_scalar_<name> + change_of_<name> * timestep_fraction 
              </tracers>                         
                            

                #------------------------------------
                # STEP 6.5: output of process rates
                #------------------------------------
              <processes vertLoc=WAT; isOutput=1>
                output_vector_<name>[k] = output_vector_<name>[k] + <name> * timestep_fraction * fraction_of_total_timestep 
              </processes>
                if (k == kmax-1):
                    cgt_dummyvar = 0.0
                  <processes vertLoc=SED; isOutput=1>
                    output_scalar_<name> = output_scalar_<name> + <name> * timestep_fraction * fraction_of_total_timestep 
                  </processes>
                 
                if (k == 1):
                    cgt_dummyvar = 0.0
                  <processes vertLoc=SUR; isOutput=1>
                    output_scalar_<name> = output_scalar_<name> + <name> * timestep_fraction * fraction_of_total_timestep 
                  </processes>
                 
             
                #------------------------------------
                # STEP 6.6: set timestep to remaining timestep only
                #------------------------------------

                cgt_timestep = cgt_timestep * (1.0 - timestep_fraction)                           # remaining timestep
                fraction_of_total_timestep = fraction_of_total_timestep * (1.0 - timestep_fraction)   # how much of the original timestep is remaining


                if (number_of_loop > 100):
                    error('aborted positive-definite scheme: more than 100 iterations') 
                 
                number_of_loop=number_of_loop+1 

              
            #------------------------------------
            #-- END OF POSITIVE-DEFINITE SCHEME -
            #------------------------------------  
             
            #------------------------------------
            # STEP 7.1: output of new tracer concentrations
            #------------------------------------
          <tracers vertLoc=WAT; isOutput=1>
            output_vector_<name>[k] = output_vector_<name>[k] + <name> 
          </tracers>
            if (k == kmax-1):
                cgt_dummyvar = 0.0
              <tracers vertLoc=SED; isOutput=1>
                output_scalar_<name> = output_scalar_<name> + <name> 
              </tracers>
              
            if (k==0):
                cgt_dummyvar = 0.0
              <tracers vertLoc=SUR; isOutput=1>
                output_scalar_<name> = output_scalar_<name> + <name> 
              </tracers>
              
             
            #------------------------------------
            # STEP 7.2: calculate "late" auxiliaries
            #------------------------------------
          <auxiliaries vertLoc=WAT; calcAfterProcesses=1>
            # <description> :
            temp1  = <temp1> 
            temp2  = <temp2> 
            temp3  = <temp3> 
            temp4  = <temp4> 
            temp5  = <temp5> 
            temp6  = <temp6> 
            temp7  = <temp7> 
            temp8  = <temp8> 
            temp9  = <temp9> 
            <name> = <formula> 
             
          </auxiliaries>

            if (k == kmax-1):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SED; calcAfterProcesses=1>
                # <description> :
                temp1  = <temp1> 
                temp2  = <temp2> 
                temp3  = <temp3> 
                temp4  = <temp4> 
                temp5  = <temp5> 
                temp6  = <temp6> 
                temp7  = <temp7> 
                temp8  = <temp8> 
                temp9  = <temp9> 
                <name> = <formula> 
                
             </auxiliaries>
              
             
            if (k == 0):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SUR; calcAfterProcesses=1>
                # <description> :
                temp1  = <temp1> 
                temp2  = <temp2> 
                temp3  = <temp3> 
                temp4  = <temp4> 
                temp5  = <temp5> 
                temp6  = <temp6> 
                temp7  = <temp7> 
                temp8  = <temp8> 
                temp9  = <temp9> 
                <name> = <formula> 
                
              </auxiliaries>
              
             
            #------------------------------------
            # STEP 7.3: output of "late" auxiliaries
            #------------------------------------
          <auxiliaries vertLoc=WAT; calcAfterProcesses=1; isOutput=1>             
            output_vector_<name>[k] = output_vector_<name>[k] + <name> 
          </auxiliaries>
          <auxiliaries vertLoc=WAT; calcAfterProcesses=1; isUsedElsewhere=1>             
            auxiliary_vector_<name>[k] = <name> 
          </auxiliaries>
            if (k == kmax-1):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SED; calcAfterProcesses=1; isOutput=1>
                output_scalar_<name> = output_scalar_<name> + <name> 
              </auxiliaries>
              <auxiliaries vertLoc=WAT; calcAfterProcesses=1; isUsedElsewhere=1>             
                auxiliary_scalar_<name> = <name> 
              </auxiliaries>
              
            if (k == 0):
                cgt_dummyvar = 0.0
              <auxiliaries vertLoc=SUR; calcAfterProcesses=1; isOutput=1>
                output_scalar_<name> = output_scalar_<name> + <name> 
              </auxiliaries>
              <auxiliaries vertLoc=SUR; calcAfterProcesses=1; isUsedElsewhere=1>             
                auxiliary_scalar_<name> = <name> 
              </auxiliaries>
              

            #---------------------------------------
            # STEP 7.4: passing vertical velocity and diffusivity to the coupler
            #---------------------------------------

            # EXPLICIT MOVEMENT
          <tracers vertLoc=WAT; vertSpeed/=0>
            vertical_speed_of_<name>[k]=(<vertSpeed>)/(24*3600.0)   # convert to m/s
            vertical_diffusivity_of_<name>[k]=(<vertDiff>)          # leave as m2/s
          </tracers> 
     
    
    #---------------------------------------
    # biological timestep has ended
    #---------------------------------------
    
    #---------------------------------------
    # vertical movement follows
    #---------------------------------------
    
    # calculate new total marked element concentrations
    for k in range(kmax):
        cgt_dummyvar = 0.0
      <celements>
        tracer_vector_<total>[k] = (
          <containingTracers vertLoc=WAT>
             max(0.0,tracer_vector_<ct>[k])*<ctAmount> + 
          </containingTracers>
                0.0 )
      </celements>
     
    
    # vertical movement of tracers
    for m in range(num_vmove_steps):
        # first, move the age concentration of marked elements
      <tracers childOf/=none; vertLoc=WAT; vertSpeed/=0; hasCeAged>
        tracer_vector_<ceAgedName> = vmove_explicit(vertical_speed_of_<name>, 
                         tracer_vector_<ceAgedName>, 
                         tracer_vector_<name>, tracer_vector_<ceTotalName>, 
                         cellheights, timestep/num_vmove_steps*(24*3600)) 

      </tracers>
        # second, move the tracers (including marked tracers) themselves
      <tracers vertLoc=WAT; vertSpeed/=0>
        tracer_vector_<name> = vmove_explicit(vertical_speed_of_<name>, 
                                   tracer_vector_<name>, 
                                   tracer_vector_<name>, tracer_vector_<name>, 
                                   cellheights, timestep/num_vmove_steps*(24*3600)) 
      </tracers>
        # third, calculate new total marked element concentrations
        for k  in range(kmax):
            cgt_dummyvar = 0.0
          <celements>
            tracer_vector_<total>[k] = (
              <containingTracers vertLoc=WAT>
                max(0.0,tracer_vector_<ct>[k])*<ctAmount> + 
              </containingTracers>
                    0.0 )
          </celements>       
        
     
    # vertical diffusion of tracers
    for m in range(num_vmove_steps):
        # first, diffuse the age concentration of marked elements
      <tracers childOf/=none; vertLoc=WAT; vertSpeed/=0; hasCeAged>
        tracer_vector_<ceAgedName> = vdiff_explicit(vertical_diffusivity_of_<name>, 
                                   tracer_vector_<ceAgedName>, 
                                   tracer_vector_<name>, tracer_vector_<ceTotalName>, 
                                   cellheights, timestep/num_vmove_steps*(24*3600)) 

      </tracers>
        # second, diffuse the tracers (including marked tracers) themselves
      <tracers vertLoc=WAT; vertSpeed/=0>
        tracer_vector_<name> = vdiff_explicit(vertical_diffusivity_of_<name>, 
                                   tracer_vector_<name>, 
                                   tracer_vector_<name>, tracer_vector_<name>, 
                                   cellheights, timestep/num_vmove_steps*(24*3600)) 
      </tracers>
        # third, calculate new total marked element concentrations
        for k  in range(kmax):
            cgt_dummyvar = 0.0
          <celements>
            tracer_vector_<total>[k] = (
              <containingTracers vertLoc=WAT>
                max(0.0,tracer_vector_<ct>[k])*<ctAmount> + 
              </containingTracers>
                    0.0 )
          </celements>       
        
     

    # calculate total colored element concentrations at bottom
  <celements>
    tracer_scalar_<totalBottom> = (
      <containingTracers vertLoc=SED>
        max(0.0,tracer_scalar_<name>)*<ctAmount> + 
      </containingTracers>
            0.0 )
  </celements>
