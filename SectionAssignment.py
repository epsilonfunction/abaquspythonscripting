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

def SectionAssignment(part_name,section_name,findAt_length):

    mdb.models['Model-1'].parts[part_name].SectionAssignment(
        
        offset=0.0, 
        offsetField='', 
        offsetType=MIDDLE_SURFACE, 
        
        region=Region(
            faces=mdb.models['Model-1'].parts[part_name].faces.findAt(
                ((findAt_length,findAt_length, 0.0),
                 (0.0, 0.0, 1.0)), 
            )
        ), 
        
        sectionName=section_name, 
        thicknessAssignment=FROM_SECTION
    )