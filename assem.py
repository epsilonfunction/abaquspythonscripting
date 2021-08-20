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

def create_instance(new_instance_name,part_name):
    #create instance of part 

    mdb.models['Model-1'].rootAssembly.Instance(    
        dependent=ON,
        
        name=new_instance_name,

        part=mdb.models['Model-1'].parts[part_name]
    )

def translate(part_name, translation_vector): #Vector to be given in (x,y,z)
    
    mdb.models['Model-1'].rootAssembly.translate(
        instanceList=(part_name, ), 
        vector=translation_vector
    )

def assembly_merge(instance_master,instance_slave,new_part_name):
    
    mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(
        
        domain=GEOMETRY, 
        
        instances=(
            mdb.models['Model-1'].rootAssembly.instances[instance_master], 
            mdb.models['Model-1'].rootAssembly.instances[instance_slave]
        ), 
    
        keepIntersections=ON,
        
        name=new_part_name,
        
        originalInstances=DELETE)#Deletes original instance | SUPPRESS to keep originals

    return