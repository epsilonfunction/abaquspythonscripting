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

def create_set(part,position,name_1):
    mdb.models['Model-1'].parts[part].Set(
        cells=mdb.models['Model-1'].parts[part].cells.findAt(
            (position, )),
            name=name_1
        )
    return

def change_set_name(part,oldName,newName):
    mdb.models['Model-1'].parts[part].sets.changeKey(
        fromName=oldName, 
        toName=newName
    )
