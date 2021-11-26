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

from math import sin,cos,radians

import Loading.loading as loading
import Jobs.setjob as setjob

loading_angles=[5.0*i for i in range(19)]

first_step='Step-1'

loading.create_step(first_step,"Initial")

#Surface
loading.create_load("Pressure","top",first_step,"Load-1",1000.0,'final-1')
loading.create_load("Pressure","right",first_step,"Load-2",0.01,'final-1')

#Set
loading.setBC("Displacement","bottom",first_step,"BC-1","final-1",0.0,0.0,0.0)
allforce = {} #dictionary of all forces

for j in loading_angles[1:]:

    try:
        loading.setload("Load-1",1000.0*cos(radians(j)))
    except:
        loading.setload("Load-1",0.01)

    try:
        loading.setload("Load-2",1000.0*sin(radians(j)))
    except:
        loading.setload("Load-2",0.01)

    
    job_name="Biaxial_Loading_1000N_"+str(int(j))+"degrees"
    print(job_name)
    setjob.inp_only(job_name)
    setjob.create_job(job_name)
    # setjob.submit_job(job_name)
    setjob.wait_till_complete(job_name)