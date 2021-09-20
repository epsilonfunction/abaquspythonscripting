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

def set_coord(part_name,coord_name,coords)
    mdb.models['Model-1'].parts[part_name].DatumCsysByThreePoints(
        coordSysType=CARTESIAN, 
        name=coord_name, 
        origin=(0.0, 0.0, 0.0), 
        point1=coords[1], 
        point2=coords[2]
    )