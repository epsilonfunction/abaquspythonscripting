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
global working_instance

#Editable
global global_length
global global_matrix_size

global_length = 1.0
global_matrix_size = (1,5)

polygon_centres = polygon_matrix.matrix_centres(
    1,0,global_length,'hexagon')
materials = material_creation_and_section.generate_materials(mp) #parameters fixed
#print(materials)

new_hexagon_points=polygon_matrix.hexagon(global_length,(0.0,0.0))
print(new_hexagon_points)
polygon_creation.polygon("new",new_hexagon_points,'two',1.0)
#polygon_creation.polygon("new",new_hexagon_points,'three',1.0)

base_part=[]
set_list=[]
for i in range(len(mp)):

    master="new"
    slave="Part-"+mp[i][2]

    clone_parts.clone(master,slave)
    
    mdb.models['Model-1'].parts[slave].Set(
        faces=mdb.models['Model-1'].parts[slave].faces.findAt(
            ((0,0,0),(0,0,0))
        ),
        name="set"+mp[i][2]
    )

    base_part.append([slave]+materials[i])

print(base_part)

def binary_set(number):
    if number > 0:
        number = 0
    elif number == 0:
        number += 1
    return number

binary_counter = 0
counter = random.randrange(0,3)

print(polygon_centres)

for i in range(1,len(polygon_centres)):
    counter += 1

    if counter >= 3:
        counter = 0
    
    if i == 1:
        
        master=base_part[0][0]
        slave_added = base_part[counter][0]

        print("adding first instance")

    else:
        master="Main"+str(binary_counter)
        slave_added = base_part[counter][0]

        print("Now adding "+slave_added+ "to "+master)
    
    main_instance = "maininstance"
    slave_instance = "slaveinstance-Part#"+str(counter)

    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    
    assem.create_instance(main_instance,master)
    assem.create_instance(slave_instance,slave_added)
        
    translation_cntr = list(polygon_centres[i])
    translation_cntr.append(0.0)

    vector_trans = tuple(translation_cntr)
    assem.translate(slave_instance, vector_trans)

    old_binary = binary_counter
    binary_counter = binary_set(binary_counter)

    working_instance="Main"+str(binary_counter)+'-1'
    assem.assembly_merge(main_instance,slave_instance,"Main"+str(binary_counter))

    #Bad Coding Practices below. See at your own risk
    try:
        del mdb.models['Model-1'].parts['Main'+str(old_binary)]
    except:
        pass
    #Problem of repeating instances | Not sure why. Seems to work fine either ways.
    #Will like to cleanup soon.
    try:
        del mdb.models['Model-1'].rootAssembly.features['Main'+str(old_binary)+'-1']
        print("Successful")
    except:
        print("Exception Occured")

    # print(slave_instance+" is added to "+main_instance)

print(working_instance)