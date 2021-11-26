#Created by Jia Yuan on 11 Nov 2021
#Inputs: NONE
#Outputs: NONE
#Editable: NONE
#Description: One Stop file to run everything; To Replace Main


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
import tempsix
#Local Subroutine Folders
from Meshing import meshing as msh

#Local Parameters file
# import TestCase.peepee

#Local Parameters Folder
from Parameters.Parameter import material_parameters as mp, gamma_variant as gv, alpha_variant as av
from Parameters import Preset_Lib as pp_lib, RVE_Surface_Para as Surf_Para


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

global_length = 150.0   #half-length of lamellae
global_height = 25.0    #Width of Lamellae
global_matrix_size = (1,5) #Depreciated

geomsize=(779.4,450.0,150.0) #Size of polycolony in x,z,y format
maxdist=max(geomsize)

"""
All useful functions here
"""
def binary_set(number):
    if number > 0:
        number = 0
    elif number == 0:
        number += 1
    return number

"""
Scripting Begins Here
"""
polygon_centres=polygon_matrix.hexa_all((0.0,0.0),global_length,maxdist/math.sqrt(2),3)
polygon_centres_dict={}
all_intersects=[]

for i in range(len(polygon_centres)):

    layer_2_dict={}
    
    for j in polygon_centres[i]:
        listofvertex=polygon_matrix.hexagon(global_length,j)

        for k in listofvertex:
            add_bool=1
            for m in all_intersects:
                if ( ((k[0]-m[0])**2) + ((k[1]-m[1])**2) ) <= 1.0:
                    listofvertex[listofvertex.index(k)]=m
                    add_bool=0
                    print("Replaced "+str(k)+" with "+str(m))
            if add_bool==1:
                all_intersects.append(k)

        layer_2_dict[j]=listofvertex
                                    
    polygon_centres_dict[i]=layer_2_dict

first_bool,overall_counter=0,0
main_name=0
parts_list=[]
prev_master_name,new_master_name,slave_name='null','null','null'
for i in polygon_centres_dict:
    for j in polygon_centres_dict[i]:
        
        prev_master_name=new_master_name
        print(j,polygon_centres_dict[i][j])

        toadd_part=tempsix.tempfull(
            geomsize,global_height,j,polygon_centres_dict[i][j]
        )        
        
        slave_name="to_add"
        mdb.models['Model-1'].parts.changeKey(
                fromName=toadd_part,
                toName=slave_name
            )

        # polygon_creation.polygon(
        #     slave_name,polygon_centres_dict[i][j],'three',global_height
        # )
        
        
        if first_bool==0:
            first_bool+=1
            mdb.models['Model-1'].parts.changeKey(
                fromName='to_add',
                toName='main0'
            )
            
            assem.create_instance('main0-1','main0')
            new_master_name='main0'
        
        else:
            
            new_master_name='main'+str(main_name)
            
            assem.create_instance('to_add','to_add')
            
            assem.translate('to_add',(0.0,0.0,int(i)*2.0*global_height))
            assem.assembly_merge(prev_master_name+'-1',"to_add",new_master_name)
            
            delete_ops.delete(prev_master_name,'part')
            delete_ops.delete('to_add','part')
            
        main_name=binary_set(main_name)
        overall_counter+=1

print(new_master_name)
new_master_instance=new_master_name+'-1'

working_part,working_instance=[new_master_name],[new_master_instance]
major_dist=maxdist*2.0
major_dist=max(major_dist,1000.0)

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
assem.translate(new_master_instance,(0.0,0.0,12.0*global_height))

assem.assembly_cut('minor','major','mold')
working_part+=['minor','major','mold','alpha_2','final']
working_instance.append('mold-1')

assem.assem_rotate(working_instance[0],90.0,(1.0,0.0,0.0))
assem.assem_rotate(working_instance[1],90.0,(1.0,0.0,0.0))

assem.assembly_cut(working_instance[1],working_instance[0],'Interest')
working_part.append('Interest')
working_instance.append('Interest-1')

#Adding Alpha2 layer
alpha_2_layer=geomsize[:2]+(global_height, )
points_alpha2=  [(0.0+alpha_2_layer[0]/2.0,0.0+alpha_2_layer[1]/2.0),
                (0.0+alpha_2_layer[0]/2.0,0.0-alpha_2_layer[1]/2.0),
                (0.0-alpha_2_layer[0]/2.0,0.0-alpha_2_layer[1]/2.0),
                (0.0-alpha_2_layer[0]/2.0,0.0+alpha_2_layer[1]/2.0)
            ]
polygon_creation.polygon('alpha_2',points_alpha2,'three',alpha_2_layer[2])
set_ops.create_set('alpha_2', 'Alpha_2', (0.0,0.0,0.0), 'region')
assem.create_instance('alpha_2-1', 'alpha_2')
assem.assem_rotate('alpha_2-1',90,(1.0,0.0,0.0))


assem.assembly_merge('Interest-1','alpha_2-1','final')

print(working_part)
for i in working_part:
    if i != 'final':
        delete_ops.delete(i,'part')
print(working_part)

pp_lib.fn()

surface_dict= {
        'top':Surf_Para.top_surf(geomsize,global_length,global_height),
        'bottom':Surf_Para.bot_surf(geomsize,global_length,global_height),
        'left':Surf_Para.left_surf_grp(geomsize,global_length,global_height),
        'right':Surf_Para.right_surf_grp(geomsize,global_length,global_height),
        'front':Surf_Para.front_surf_grp(geomsize,global_length,global_height),
        'back':Surf_Para.back_surf_grp(geomsize,global_length,global_height)
    }


Surface_Ops.Surface_Main.setallsurf('final',surface_dict)
temp_region_set.setallsurf('final',surface_dict,'surface')

import TestMesh as TM
top_list=surface_dict['top']
first_bool=0
lengthcount,dx = 0.0,0.2
while lengthcount <= geomsize[2]:
    
    extra=[]
    extra.append(lengthcount+dx)
    
    if first_bool==0:
        first_bool+=1

    else:
        extra.append(lengthcount-dx)
        
    for i in top_list:
        for j in extra:
            p = []
            for k in i:
                p.append(k)
            p[1]=j
            p = tuple(p)
            TM.mesh_control('final',p)
            
    lengthcount+=global_height
for i in top_list:
    p=[]
    for k in i:
        p.append(k)
    p[1]=(-1.0*(global_height/2.0))
    p = tuple(p)
    TM.mesh_control('final',p)

TM.seeding('final',0.1,0.1,25)
TM.gen_mesh('final')
