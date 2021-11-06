from abaqus import *
from abaqusConstants import *

from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# from ..Parameters import RVE_Surface_Para as Surf_Para

# global_length = 150.0   #half-length of lamellae
# global_height = 25.0    #Width of Lamellae

# geomsize=(779.4,450.0,150.0) #Size of polycolony 

# a = Surfaces.top_surf(geocmsize,global_length)

# b = Surfaces.left_surf_grp(geomsize,global_length,global_height)
# b.append((geomsize[0]/2.0,-1*global_height/2.0,0.0))

def create_surf(part_name, new_surf_name, face_coord):
    #face_coord: type(tuple)
    #part_name,new_surf_name: type(string)
    mdb.models['Model-1'].parts[part_name].Surface(
        name=new_surf_name, 
        
        side1Faces= 
        mdb.models['Model-1'].parts[part_name].faces.findAt(
            
            (
                face_coord,
            ),
        )
    )

    return

def boolmerge_surf(part_name,new_surf_name,to_merge_surf_1,to_merge_surf_2):
    mdb.models['Model-1'].parts[part_name].SurfaceByBoolean(
        name=new_surf_name, 
        surfaces=(
            mdb.models['Model-1'].parts[part_name].surfaces[to_merge_surf_1], 
            mdb.models['Model-1'].parts[part_name].surfaces[to_merge_surf_2]
        )
    )
    return


def setsurf(part_name,surface_name,string_of_surface):

    length_of_string=len(string_of_surface)
    for i in range(length_of_string):
        to_add_surf_name='ToAddSurf-'+str(i)
        face_coord=string_of_surface[i]

        create_surf(part_name,to_add_surf_name,face_coord)

        if i==0:
            continue
        elif i == 1:
            boolmerge_surf(part_name,surface_name,"ToAddSurf-0",to_add_surf_name)
            del mdb.models['Model-1'].parts[part_name].surfaces["ToAddSurf-0"]
        else:
            boolmerge_surf(part_name,surface_name,surface_name,to_add_surf_name)
        
        del mdb.models['Model-1'].parts[part_name].surfaces[to_add_surf_name]

    print("Added "+str(surface_name)+" to "+str(part_name))
    return

# def fn(part_name,geomsize,global_length,global_height):

#     all_surface_parameters = {
#         'top':Surf_Para.top_surf(geomsize,global_length),
#         'bottom':Surf_Para.bot_surf(global_height),
#         'left':Surf_Para.left_surf_grp(geomsize,global_length,global_height),
#         'right':Surf_Para.right_surf_grp(geomsize,global_length,global_height),
#         'front':Surf_Para.front_surf_grp(geomsize,global_length,global_height),
#         'back':Surf_Para.back_surf_grp(geomsize,global_length,global_height)
#     }

#     for i in all_surface_parameters:
#         setsurf(part_name,str[i],all_surface_parameters[i])

#     return all_surface_parameters

############### SETS BELOW #####################
"""
    Not Done Here
    
    Done in set_ops
    
"""
