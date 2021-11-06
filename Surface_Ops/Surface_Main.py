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
import Surface_Ops 

def setallsurf(part_name,all_surface_parameters):

#     all_surface_parameters = {
#         'top':Surf_Para.top_surf(geomsize,global_length),
#         'bottom':Surf_Para.bot_surf(global_height),
#         'left':Surf_Para.left_surf_grp(geomsize,global_length,global_height),
#         'right':Surf_Para.right_surf_grp(geomsize,global_length,global_height),
#         'front':Surf_Para.front_surf_grp(geomsize,global_length,global_height),
#         'back':Surf_Para.back_surf_grp(geomsize,global_length,global_height)
#     }

    for i in all_surface_parameters:
        Surface_Ops.setsurf(part_name,str[i],all_surface_parameters[i])

    return
