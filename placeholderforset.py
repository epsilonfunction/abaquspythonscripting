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

def fn(height):
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Gamma-I-M-1', 
        part=mdb.models['Model-1'].parts['Gamma-I-M'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Gamma-I-T-1', 
        part=mdb.models['Model-1'].parts['Gamma-I-T'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Gamma-II-M-1', 
        part=mdb.models['Model-1'].parts['Gamma-II-M'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Gamma-II-T-1', 
        part=mdb.models['Model-1'].parts['Gamma-II-T'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Gamma-III-M-1', 
        part=mdb.models['Model-1'].parts['Gamma-III-M'])
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Gamma-III-T-1', 
        part=mdb.models['Model-1'].parts['Gamma-III-T'])
    mdb.models['Model-1'].rootAssembly.translate(instanceList=(
        'Gamma-I-T-1', 
        'Gamma-II-T-1', 
        'Gamma-III-T-1',
        'Gamma-I-M-1',
        'Gamma-II-M-1',
        'Gamma-III-M-1'), vector=(0.0, 0.0, -1.0*height))
    mdb.models['Model-1'].rootAssembly.translate(instanceList=('Gamma-I-T-1', 
        'Gamma-II-T-1', 'Gamma-III-T-1'), vector=(0.0, 0.0, -1.0*height))
    mdb.models['Model-1'].rootAssembly.translate(instanceList=('Gamma-II-M-1', 
        'Gamma-II-T-1', 'Gamma-III-M-1', 'Gamma-III-T-1'), vector=(0.0, 0.0, 
        -2.0*height))
    mdb.models['Model-1'].rootAssembly.translate(instanceList=('Gamma-III-M-1', 
        'Gamma-III-T-1'), vector=(0.0, 0.0, -2.0*height))
    mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
        instances=(mdb.models['Model-1'].rootAssembly.instances['Gamma-I-M-1'], 
        mdb.models['Model-1'].rootAssembly.instances['Gamma-I-T-1'], 
        mdb.models['Model-1'].rootAssembly.instances['Gamma-II-M-1'], 
        mdb.models['Model-1'].rootAssembly.instances['Gamma-II-T-1'], 
        mdb.models['Model-1'].rootAssembly.instances['Gamma-III-M-1'], 
        mdb.models['Model-1'].rootAssembly.instances['Gamma-III-T-1']), 
        keepIntersections=ON, name='tempsix', originalInstances=DELETE)
