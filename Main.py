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

#Editable
global global_length
global global_matrix_size

global_length = 1.0
global_matrix_size = (5,5)

polygon_centres = polygon_matrix.matrix_centres(global_matrix_size[0],global_matrix_size[1],global_length) #only 2d squares for now
materials = material_creation_and_section.generate_materials(mp) #parameters fixed

main_part = polygon_matrix.square(global_length,(0.0,0,0))
polygon_creation.twod_rectangle(main_part[0],main_part[1],"Main0")

base_part=[]
base_part.append(["Main0",materials[0][2]])

#Clone all materials in required dimension
for i in range(len(materials)):

    master = "Main0"
    slave = "Part-"+str(i)

    clone_parts.clone(master,slave)

    base_part.append([slave,materials[i][2]])

print(base_part) #sanity check

for j in range(len(base_part)):
    
    part_name,section_name = "",""
    findAt_length = global_length*-0.166667

    if j == 0:
        part_name="Main0"
        section_name="Section-0"

    else:
        part_name="Part-"+str(j-1)
        section_name="Section-"+str(j-1)

    SectionAssignment.SectionAssignment(
        part_name,section_name,findAt_length
    )

    base_part[j].append(section_name)

    meshing.meshing(
        part_name,findAt_length
    )

print(base_part) #sanity check

def binary_set(number):
    if number > 0:
        number = 0

    elif number == 0:
        number += 1

    return number

binary_counter = 0
counter = random.randrange(1,4)

for i in range(len(polygon_centres)):
    counter += 1

    if counter >= 3:
        counter = 1
    
    if i == 0:

        pass

    else:
        
        slave_added = "Part-"+str(counter)
        master = "Main"+str(binary_counter)

        main_instance = "maininstance"
        slave_instance = "slaveinstance-Part#"+str(counter)

        print("Now adding "+slave_instance+ "to "+main_instance)

        # clone_parts.clone(master,new_part)

        mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)

        assem.create_instance(main_instance,master)
        assem.create_instance(slave_instance,base_part[counter][0])

        translation_cntr = list(polygon_centres[i])
        translation_cntr.append(0.0)

        vector_trans = tuple(translation_cntr)
        assem.translate(slave_instance, vector_trans)

        old_binary = binary_counter
        binary_counter = binary_set(binary_counter)

        assem.assembly_merge(main_instance,slave_instance,"Main"+str(binary_counter))

        del mdb.models['Model-1'].parts['Main'+str(old_binary)]

        #Problem of repeating instances | Not sure why. Seems to work fine either ways.
        #Will like to cleanup soon.
        try:
            del mdb.models['Model-1'].rootAssembly.features['Main'+str(old_binary)+'-1']
            print("Successful")
        except:
            print("Exception Occured")

        print(slave_instance+" is added to "+main_instance)

            





#polygon_matrix.sketch_add(polygon_points)
#print(polygon_points)

#DONE: material_creation import | -DONE- on 4th Aug 2021. 
#TODO: section_creation import
#TODO: geometry_import

