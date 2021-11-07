import set_ops

def setallsurf(part_name,all_surface_parameters,set_type):
    
    if set_type=='surface':
        for i in all_surface_parameters:
            set_ops.setgrp(part_name,i,all_surface_parameters[i])
        
    return
