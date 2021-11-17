
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
import random as random
import numpy as np

#Local Subroutine Imports
import material_creation_and_section
import polygon_matrix
import polygon_creation
import clone_parts
import SectionAssignment
import assem
import set_ops
import Surface_Ops.Surface_Main
import placeholderforset
import temp_region_set
import delete_ops as delete_ops

from Parameters.Parameter import gamma_variant as gv


def binary_set(number):
    if number > 0:
        number = 0
    elif number == 0:
        number += 1
    return number

def tempsix(points_centre,points_list,global_height):
    
    set_list,base_part=[],[]
    
    polygon_creation.polygon(
        "new",points_list,'three',global_height
    )

    origin_alt=(list(points_centre)+[global_height/2.0])
    set_ops.create_set("new","original",origin_alt,"region")
    
    binary_counter = 0
    
    for i in range(len(gv)):
        master="new"
        slave=gv[i][0]
        slave_set_name=gv[i][0]
        
        clone_parts.clone(master,slave)
        
        set_ops.change_set_name(slave,"original",slave_set_name)
        set_list.append(slave_set_name)
        base_part.append(slave_set_name)

    first_bool,main_name,counter = 0,0,0.0
    prev_master_name,new_master_name,slave_name='null','null','null'
    for i in base_part:
        prev_master_name=new_master_name
        slave_name=i+'-1'
        assem.create_instance(slave_name,i) #name,part

        if first_bool==0:
            first_bool+=1
            
            new_master_name=i
                        
        else:
            new_master_name='tempsix'+str(main_name)
            assem.translate(
                slave_name,
                (0.0,0.0,int(counter)*-1.0*global_height)
            )
            assem.assembly_merge(
                prev_master_name+'-1',
                slave_name,
                new_master_name
            )            
        
        main_name=binary_set(main_name)
        counter+=1.0
        if new_master_name not in base_part:
            base_part.append(new_master_name)
    
    base_part.append('new')

    for i in base_part:
        if i != new_master_name:
            delete_ops.delete(i,'part')
    assem.delete_instance(new_master_name+'-1')
    return new_master_name


def tempfull(rve_size,global_height,points_centre,points_list):

    maxdist=max(rve_size)
    mingeomheightmultiple=int(math.floor(maxdist/(6*global_height)))+2
    
    first_bool,main_name,counter = 0,0,0.0
    prev_master_part,prev_master_inst='null','null'
    new_master_part,new_master_inst='null','null'
    slave_part,slave_inst='tempsix','null'
    part_name=tempsix(points_centre,points_list,global_height) 
    
    mdb.models['Model-1'].parts.changeKey(
                fromName=part_name,
                toName=slave_part
            )
    
    for i in range(mingeomheightmultiple):
        prev_master_part=new_master_part
        prev_master_inst=new_master_inst
        slave_inst=slave_part+'-'+str(i)
        assem.create_instance(slave_inst,slave_part)

        if first_bool==0:
            first_bool+= 1
            new_master_inst=slave_inst           
        
        else:
            new_master_part='tempfull'+str(main_name)
            assem.translate(
                slave_inst,
                (0.0,0.0,-6.0*counter*global_height)
            )
            assem.assembly_merge(
                prev_master_inst,slave_inst,new_master_part
            )
            new_master_inst=new_master_part+'-1'
            main_name=binary_set(main_name)
            try:
                delete_ops.delete(prev_master_part,'part')
            except:
                pass
                    
        counter += 1.0
    
    delete_ops.delete(slave_part,'part')

    return part_name



# tempfull(
    
#     (779.4,450.0,150.0),
#     25.0,
        
#     (519.61, 450.0),
#     [   (519.6, 600.0), 
#         (389.7, 525.0), 
#         (389.7, 375.0), 
#         (519.6, 300.0), 
#         (649.5, 375.0), 
#         (649.5, 525.0)
#     ]
#     )
# (
#     (519.61, 450.0), 
#     [   (519.6, 600.0), 
#         (389.7, 525.0), 
#         (389.7, 375.0), 
#         (519.6, 300.0), 
#         (649.5, 375.0), 
#         (649.5, 525.0)
#     ], 
    
# 1)

# slave_name="to_add"
# prev_master_name=new_master_name
# listofvertex=polygon_centres_dict[i][j]

# slave_part,slave_instance_name=tempsix.tempfull(
#     geomsize,global_height,j,listofvertex
# )
# delete_ops.delete(slave_instance_name,'instance')
# # polygon_creation.polygon(
# #     slave_name,polygon_centres_dict[i][j],'three',global_height
# # )

# mdb.models['Model-1'].parts.changeKey(
#         fromName=slave_part,
#         toName='to_add'
#     )        

# if first_bool==0:
#     first_bool+=1
#     mdb.models['Model-1'].parts.changeKey(
#         fromName='to_add',
#         toName='main0'
#     )
    
#     assem.create_instance('main0-1','main0')
#     new_master_name='main0'

# else:
    
#     new_master_name='main'+str(main_name)
    
#     assem.create_instance('to_add','to_add')
#     assem.translate('to_add',(0.0,0.0,int(i)*2.0*global_height))
#     assem.assembly_merge(prev_master_name+'-1',"to_add",new_master_name)
    
#     delete_ops.delete(prev_master_name,'part')

# main_name=binary_set(main_name)