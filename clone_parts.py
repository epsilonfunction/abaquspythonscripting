
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *

def clone(clone_master_name,clone_slave_name):
    
    master=mdb.models['Model-1'].parts[clone_master_name]
    
    mdb.models['Model-1'].Part(
        name=clone_slave_name,
        objectToCopy=master
    )