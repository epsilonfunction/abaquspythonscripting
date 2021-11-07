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

def meshing(part_name,coord,element_shape,element_technique):

    mdb.models['Model-1'].parts[part_name].setMeshControls(
        
        elemShape=element_shape,
        technique=element_technique,

        regions=mdb.models['Model-1'].parts[part_name].faces.findAt(
            (
                (findAt_length, findAt_length,0.0), 
            )
        ) 
    )
    
    mdb.models['Model-1'].parts[part_name].setElementType(
        
        elemTypes=(
            ElemType(
                elemCode=CPS8R, 
                elemLibrary=STANDARD
            ),

            ElemType(
                elemCode=CPS6M,
                elemLibrary=STANDARD)
            ), 
        
        regions=(
            mdb.models['Model-1'].parts[part_name].faces.findAt(
                (
                    (findAt_length, findAt_length,0.0),
                )
            ),
        )
    )

    mdb.models['Model-1'].parts[part_name].seedPart(
        deviationFactor=0.1, 
        minSizeFactor=0.1, 
        size=0.5
    )
    
    mdb.models['Model-1'].parts[part_name].generateMesh()