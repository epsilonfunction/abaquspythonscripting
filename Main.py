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

#Standard Python Packages
import math

#Local Subroutine Imports
import material_creation_and_section
import polygon_matrix
import polygon_creation
import clone_parts
import SectionAssignment
import meshing
import assem
import set_ops

import placeholderforset

#Local Parameters file
from Parameters import material_parameters as mp, gamma_variant as gv, alpha_variant as av

#Noneditable
global polygon_centres  #list
global materials        #list
global main_part        
global base_part
global set_list
global working_instance

#Editable
global global_length
global global_height
global global_matrix_size

global_length = 150.0   #Length of Polygon
global_height = 25.0    #Width of Lamellae
global_matrix_size = (1,5) #Depreciated

geomsize=(780.0,450.0,150.0)
maxdist=max(geomsize)

# polygon_centres = polygon_matrix.matrix_centres(
#     1,0,global_length,'hexagon')
materials = material_creation_and_section.generate_materials(
    mp,"ORTHO") #parameters fixed
#print(materials)

new_hexagon_points=polygon_matrix.hexagon(global_length,(0.0,0.0))
print(new_hexagon_points)
#polygon_creation.polygon("new",new_hexagon_points,'two',1.0)
polygon_creation.polygon("new",new_hexagon_points,'three',global_height)

set_ops.create_set("new",(0.0,0.0,0.0),"original")

base_part=[]
set_list=[]

def binary_set(number):
    if number > 0:
        number = 0
    elif number == 0:
        number += 1
    return number

binary_counter = 0

for i in range(len(gv)):


    master="new"
    slave=gv[i][0]
    slave_set_name=gv[i][0]
        
    clone_parts.clone(master,slave)
    
    set_ops.change_set_name(slave,"original",slave_set_name)
    set_list.append(slave_set_name)
    base_part.append(slave_set_name)

#Prev Implementation of 6stack
    # slv_inst_name=slave+'-1'
    # assem.create_instance(slv_inst_name,slave)

    # temp_name='temp'+str(binary_counter)
    # temp_inst=temp_name+'-1'

    # if i ==0:
    #     working_instance.append(slv_inst_name)
    # elif i == 1:
    #     trans_vect=(0.0,0.0,-i*global_height)
    #     assem.translate(slv_inst_name,trans_vect)
    #     assem.assembly_merge(working_instance[0], slv_inst_name, temp_name)
    #     binary_counter=binary_set(binary_counter)

    # else:
        
    #     assem.assembly_merge(working_instance[0], slv_inst_name, temp_name)
    #     working_instance[0]=temp_inst
    #     binary_counter=binary_set(binary_counter)

print(base_part)
binary_counter=0

working_part=[]
working_instance=[]

# counter=0
# for i in base_part:

#     inst_name=i+'-1'
#     assem.create_instance(inst_name,i)
#     working_instance.append(inst_name)

#     temp_name='temp'+str(binary_counter)
#     temp_inst=temp_name+'-1'

#     assem.create_instance(inst_name,slave)
#     if counter == 0:
#         pass
#     else:
#         trans_vect=(0.0,0.0,-counter*global_height)
#         assem.translate(inst_name,trans_vect)
#         assem.assembly_merge(working_instance[0],working_instance[1],temp_name)
#         working_instance=[]
#         working_instance.append(temp_inst)
#         # del mdb.models['Model-1'].rootAssembly.features[temp_name]
    
#     print('adding:'+inst_name+'to'+temp_name)
#     counter+=1

#     binary_counter=binary_set(binary_counter)

placeholderforset.fn(global_height)
temp_name='tempsix'

working_part.append(temp_name)

mingeomheightmultiple=int(math.floor(maxdist/(6*global_height)))+2
working_instance=[]
counter,binary_counter=0,0
for i in range(mingeomheightmultiple):
    
    inst_name=working_part[0]+'-'+str(i)
    slave=working_part[0]
    assem.create_instance(inst_name,slave)
    working_instance.append(inst_name)

    tempsix_name='tempsix'+str(binary_counter)
    tempsix_inst=tempsix_name+'-1'

    if i == 0:
        pass
    else:
        trans_vect=(0.0,0.0,-1*i*global_height*6)
        assem.translate(inst_name,trans_vect)
        assem.assembly_merge(working_instance[0],working_instance[1],tempsix_name)
        working_instance=[tempsix_inst]

    counter+=1
    binary_counter=binary_set(binary_counter)

    print(tempsix_name)

working_part=[tempsix_name]
# assem.translate(working_instance[0],(0.0,0.0,6.0*global_height))
first_shift=(0.0,0.0,6.0*global_height)

polygon_centres=polygon_matrix.hexa_all((0.0,0.0),global_length,maxdist/math.sqrt(2),3)
print(polygon_centres)

working_instance=[]
counter,binary_counter=1,0
for i in range(3):
    z_vector=[0.0,0.0,-1.0*global_height*2.0*i]
    print(z_vector)

    for j in polygon_centres[i]:
        
        inst_name=working_part[0]+'-'+str(counter)
        slave=working_part[0]
        working_instance.append(inst_name)

        assem.create_instance(inst_name,slave)

        tempfull_name='tempfull'+str(binary_counter)
        tempfull_inst=tempfull_name+'-1'


        if j == (0.0,0.0):
            assem.translate(working_instance[0],first_shift)
        else:
            j = list(j)
            j.append(0.0)
            # print(j)
            trans_vect=[j[k]+z_vector[k]+first_shift[k] for k in range(3)]
            # assem.translate(inst_name,first_shift)
            assem.translate(inst_name,trans_vect)
            assem.assembly_merge(working_instance[0],
                                 working_instance[1],
                                 tempfull_name)
            working_instance=[tempfull_inst]

        binary_counter=binary_set(binary_counter)
        counter += 1
        
major_dist=maxdist*2.0
major_dist=max(major_dist,1000.0)
working_instance=[tempfull_inst]
points_major=[(0.0+major_dist,0.0+major_dist),(0.0+major_dist,0.0-major_dist),
             (0.0-major_dist,0.0-major_dist),(0.0-major_dist,0.0+major_dist)]
points_minor=[(0.0+geomsize[0]/2.0,0.0+geomsize[1]/2.0),
                (0.0+geomsize[0]/2.0,0.0-geomsize[1]/2.0),
                (0.0-geomsize[0]/2.0,0.0-geomsize[1]/2.0),
                (0.0-geomsize[0]/2.0,0.0+geomsize[1]/2.0)]

#Truncating our model where needed with sufficiently large mold
polygon_creation.polygon('major',points_major,'three',major_dist*2.0)
polygon_creation.polygon('minor',points_minor,'three',geomsize[2])

assem.create_instance('major','major')
assem.create_instance('minor','minor')

assem.translate('major',(0.0,0.0,-1.0*major_dist))
assem.translate('minor',(0.0,0.0,-1.0*geomsize[2]))
assem.translate(working_instance[0],(0.0,0.0,6.0*global_height))

assem.assembly_cut('minor','major','mold')
base_part.append('mold')
working_part.append('mold')
working_instance.append('mold-1')

assem.assem_rotate(working_instance[0],90.0,(1.0,0.0,0.0))
assem.assem_rotate(working_instance[1],90.0,(1.0,0.0,0.0))

assem.assembly_cut(working_instance[1],working_instance[0],'Interest')
working_part,working_instance=['Interest'],['Interest-1']

#Adding Alpha2 layer
alpha_2_layer=geomsize[:2]+(global_height, )
points_alpha2=  [(0.0+alpha_2_layer[0]/2.0,0.0+alpha_2_layer[1]/2.0),
                (0.0+alpha_2_layer[0]/2.0,0.0-alpha_2_layer[1]/2.0),
                (0.0-alpha_2_layer[0]/2.0,0.0-alpha_2_layer[1]/2.0),
                (0.0-alpha_2_layer[0]/2.0,0.0+alpha_2_layer[1]/2.0)
            ]
polygon_creation.polygon('alpha_2',points_alpha2,'three',alpha_2_layer[2])
set_ops.create_set('alpha_2', (0.0,0.0,0.0), 'Alpha_2')
assem.create_instance('alpha_2-1', 'alpha_2')
assem.assem_rotate('alpha_2-1',90,(1.0,0.0,0.0))


assem.assembly_merge('Interest-1','alpha_2-1','final')



