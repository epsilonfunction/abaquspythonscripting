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

def mesh_control(part_name,coords):
    # elemShape
        # QUAD: Quadrilateral mesh.
        # QUAD_DOMINATED: Quadrilateral-dominated mesh.
        # TRI: Triangular mesh.
        # HEX: Hexahedral mesh.
        # HEX_DOMINATED: Hex-dominated mesh.
        # TET: Tetrahedral mesh.
        # WEDGE: Wedge mesh.
    # technique
        # FREE: Free mesh technique.
        # STRUCTURED: Structured mesh technique.
        # SWEEP: Sweep mesh technique.
        # SYSTEM_ASSIGN: Allow the system to assign a suitable technique. 
            # The actual technique assigned can be STRUCTURED, SWEEP, or unmeshable.
    
    mdb.models['Model-1'].parts[part_name].setMeshControls(
        
        elemShape=TET,      #Future Variable
        technique=FREE,     #Future Variable

        regions=mdb.models['Model-1'].parts[part_name].cells.findAt(
                (coords, )
            )        
    )

def element_control(part_name,coords,coord_type):
    #ELEMTYPE
        # C3D8R, specifying a 8-node linear brick, reduced integration with hourglass control.
        # CODE, specifying add more codes.
        # UNKNOWN_TRI, specifying an unknown element type associated with a triangular shape.
        # UNKNOWN_QUAD, specifying an unknown element type associated with a quadrilateral shape.
        # UNKNOWN_HEX, specifying an unknown element type associated with a hexahedral shape.
        # UNKNOWN_WEDGE, specifying an unknown element type associated with a wedge shape.
        # UNKNOWN_TET, specifying an unknown element type associated with a tetrahedral shape.


    mdb.models['Model-1'].parts[part_name].setElementType(
        
        elemTypes=(
            ElemType(
                elemCode=C3D10, 
                elemLibrary=STANDARD
            ),

        ),
        regions=(
            mdb.models['Model-1'].parts[part_name].faces.findAt(
                (coords, )
            ),
        )
    )
    # mdb.models['Model-1'].parts[part_name].setElementType(
        
    #     elemTypes=(
    #         ElemType(
    #             elemCode=CPS8R, 
    #             elemLibrary=STANDARD
    #         ),

    #         ElemType(
    #             elemCode=CPS6M,
    #             elemLibrary=STANDARD)
    #         ), 
        
    #     regions=(
    #         mdb.models['Model-1'].parts[part_name].faces.findAt(
    #             (coords, )
    #         ),
    #     )
    # )
    
def seeding(part_name,deviation,minsize,seedsize):
    mdb.models['Model-1'].parts[part_name].seedPart(
        deviationFactor=deviation, 
        minSizeFactor=minsize, 
        size=seedsize
    )
def gen_mesh(part_name):
    mdb.models['Model-1'].parts[part_name].generateMesh()