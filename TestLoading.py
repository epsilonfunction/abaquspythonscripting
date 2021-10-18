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

from math import sin,cos

import Loading.loading as loading
import Jobs.setjob as setjob

loading_angles=[10.0*i for i in range(9)]

first_step='Step-1'

loading.create_step(first_step,"Initial")

loading.create_load("Pressure","Top",first_step,"Load-1",1000.0,'final-1')
loading.create_load("Pressure","Positive(2)",first_step,"Load-2",0.01,'final-1')

loading.setBC("Displacement","Fixed",first_step,"BC-1","final-1",0.0,0.0,0.0)
allforce = {} #dictionary of all forces
for j in loading_angles[1:]:
    pass