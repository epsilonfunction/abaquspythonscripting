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

def translate(instance_name, translation_vector): #Vector to be given in (x,y,z)
    
    mdb.models['Model-1'].rootAssembly.translate(
        instanceList=(instance_name, ), 
        vector=translation_vector
    )

def assem_rotate(instance_name,angle,axis):
    
    mdb.models['Model-1'].rootAssembly.rotate(
        angle=angle,
        axisDirection=axis,
        axisPoint=(0.0, 0.0, 0.0),
        instanceList=(instance_name, ) 
    )
    return

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

def assembly_cut(instance_cutter,instance_tocut,new_part_name):
    
    mdb.models['Model-1'].rootAssembly.InstanceFromBooleanCut(
        cuttingInstances=(
            mdb.models['Model-1'].rootAssembly.instances[instance_cutter], ), 

        instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances[instance_tocut],

        name=new_part_name,
        
        originalInstances=DELETE
    )
