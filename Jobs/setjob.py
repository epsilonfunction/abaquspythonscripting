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

def create_job(job_name):
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=DOUBLE_PLUS_PACK, getMemoryFromAnalysis=True, 
    historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE, model='Model-1', 
    modelPrint=OFF, multiprocessingMode=DEFAULT, 
    
    name=job_name, 

    nodalOutputPrecision=SINGLE, numCpus=1, numGPUs=0, queue=None, 
    resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', waitHours=
    0, waitMinutes=0)

    return

def change_job_name(old_job_name,new_job_name):

    mdb.jobs.changeKey(
        fromName=old_job_name,
        
        toName=new_job_name
    )
    return


def submit_job(job_name):
    mdb.jobs[job_name].submit(
        consistencyChecking=OFF
    )
    return