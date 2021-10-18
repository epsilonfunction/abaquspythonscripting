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

def create_step(current_step_name,previous_step_name):
    mdb.models['Model-1'].StaticStep(
        initialInc=0.01, maxInc=0.01, maxNumInc=10000, 

        name=current_step_name, 
        previous=previous_step_name,

        nlgeom=OFF
    )
    return

    
def create_load(load_type,applied_region,current_step_name,load_name,load_magnitude,instance_name):
    
    if load_type=='Pressure': #Variable
        mdb.models['Model-1'].Pressure(
            amplitude=UNSET, 
            
            createStepName=current_step_name, #Variable 
            distributionType=UNIFORM, field='', 
            
            magnitude=load_magnitude, #Variable 
            name=load_name, #Variable

            region=mdb.models['Model-1'].rootAssembly.instances[instance_name].surfaces[applied_region] #Variable
        )

    return
def setload(name,new_value):
    
    mdb.models['Model-1'].loads[name].setValues(
        magnitude=new_value
    )
    return

def setBC(BC_type,applied_region,current_step_name,BC_name,instance_name,*disp_args):

    if BC_type=='Displacement':
        disp = [i for i in disp_args]
        while len(disp) < 6:
            disp += [UNSET]
            print(disp)

        mdb.models['Model-1'].DisplacementBC(
            amplitude=UNSET, 
            
            createStepName=current_step_name,
            name=BC_name,

            distributionType=UNIFORM, fieldName='', fixed=OFF, 
            localCsys=None,  
            
            region=mdb.models['Model-1'].rootAssembly.instances[instance_name].sets[applied_region], 
            
            u1=disp[0], 
            u2=disp[1], 
            u3=disp[2], 
            ur1=disp[3], 
            ur2=disp[4], 
            ur3=disp[5]
        )
    
    return
