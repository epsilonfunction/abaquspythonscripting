#Created by Jia Yuan on 30 July 2021
#Inputs: NONE
#Outputs: NONE
#Editable: NONE
#Description: One Stop file to run everything

import random as random

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

#Local Subroutine Imports
import material_creation_and_section
import polygon_matrix
import polygon_creation
import clone_parts
import SectionAssignment
import meshing
import assem

#Local Parameters file
from Parameters import material_parameters as mp

#Noneditable
global polygon_centres  #list
global materials        #list
global main_part        
global base_part
global set_list

#Editable
global global_length
global global_matrix_size

global_length = 1.0
global_matrix_size = (1,5)

polygon_centres = polygon_matrix.matrix_centres(
    global_matrix_size[0],global_matrix_size[1],global_length,'hexagon')
materials = material_creation_and_section.generate_materials(mp) #parameters fixed

new_hexagon_points=polygon_matrix.hexagon(global_length,(0.0,0.0))
polygon_creation.twod_polygon("new",new_hexagon_points)

base_part=[]
set_list=[]
for i in range(len(materials)):

    master="new"
    slave="Part-"+materials[i][3]

    clone_parts.clone(master,slave)
    
    mdb.models['Model-1'].parts[slave].Set(
        faces=mdb.models['Model-1'].parts[part_name].faces.findAt(
            ((0,0,0),(0,0,0))
        ),
        name="set"+materials[i][2]
    )

    base_part.append([slave,materials[i[2]]])

print(base_part)

def binary_set(number):
    if number > 0:
        number = 0
    elif number == 0:
        number += 1
    return number

binary_counter = 0
counter = random.randrange(1,4)

"""
for i in range(len(polygon_centres)):
    counter += 1

    if counter >= 3:
        counter = 1
    
    if i == 0:
        
        slave_added = "Part-"+str(counter)
        master = "Main"+str(binary_counter)

        main_instance = "maininstance"
        slave_instance = "slaveinstance-Part#"+str(counter)

        mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
        assem.create_instance(master,
"""