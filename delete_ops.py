#Abaqus Imports
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

def delete(item,type):
    if type=='instance':
        del mdb.models['Model-1'].rootAssembly.features[item]
    elif type=='part':
        del mdb.models['Model-1'].parts[item]
