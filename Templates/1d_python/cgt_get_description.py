def cgt_get_description( name ):
#CGT_GET_DESCRIPTION get the description for a cgt output variable name
  
    description = '';
#  <tracers isOutput=1; isFlat=0>
#    if strcmpi(strtrim(name),strtrim('<name>'))
#        description = '<description> [mol/kg]';
#    end
#  </tracers>
#  <tracers isOutput=1; isFlat/=0>
#    if strcmpi(strtrim(name),strtrim('<name>'))
#        description = '<description> [mol/m2]';
#    end
#  </tracers>
#  <auxiliaries isOutput=1>
#    if strcmpi(strtrim(name),strtrim('<name>'))
#        description = '<description>';
#    end
#  </auxiliaries>
#  <processes isOutput=1>
#    if strcmpi(strtrim(name),strtrim('<name>'))
#        description = '<description>';
#    end
#  </processes>
    return(description)

