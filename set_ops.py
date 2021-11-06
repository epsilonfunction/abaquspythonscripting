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

#General Operations
def boolmerge_set(part_name,new_set_name,to_merge_1,to_merge_2):
    mdb.models['Model-1'].parts[part_name].SetByBoolean(
        name=new_set_name, 
        sets=(
            mdb.models['Model-1'].parts[part_name].sets[to_merge_1], 
            mdb.models['Model-1'].parts[part_name].sets[to_merge_2]
        )
    )
    return

def change_set_name(part_name,oldName,newName):
    mdb.models['Model-1'].parts[part_name].sets.changeKey(
        fromName=oldName, 
        toName=newName
    )


#Region Set
def create_set(part_name,new_set_name,coords,set_type):
    
    if set_type=='region':
        mdb.models['Model-1'].parts[part_name].Set(
            cells=mdb.models['Model-1'].parts[part_name].cells.findAt(
                (coords, )
            ),
            name=new_set_name
            )
    elif set_type=='surface':
        mdb.models['Model-1'].parts[part_name].set(
        
            side1Faces=mdb.models['Model-1'].parts[part_name].faces.findAt(
                (coords, )
            ),
            name=new_set_name
        )
    return

# #Surface Set
# def create_set_surf(part_name, new_surf_name, face_coord):
#     #face_coord: type(tuple)
#     #part_name,new_surf_name: type(string)
#     mdb.models['Model-1'].parts[part_name].set(
#         name=new_surf_name, 
        
#         side1Faces= 
#         mdb.models['Model-1'].parts[part_name].faces.findAt(
            
#             (
#                 face_coord,
#             ),
#         )
#     )

#     return




#Functional Commands

def setgrp(part_name,new_set_name,string_of_set,set_type):

    length_of_string=len(string_of_set)
    for i in range(length_of_string):
        to_add_set_name='ToAddSet-'+str(i)
        indiv_coord=string_of_set[i]

        create_set(part_name,to_add_set_name,indiv_coord,set_type)
        if i==0:
            continue
        elif i == 1:
            boolmerge_set(part_name,new_set_name,"ToAddSet-0",to_add_set_name)
            del mdb.models['Model-1'].parts[part_name].sets["ToAddSet-0"]
        else:
            boolmerge_set(part_name,new_set_name,new_set_name,to_add_set_name)
        
        del mdb.models['Model-1'].parts[part_name].sets[to_add_set_name]

    print("Added "+str(new_set_name)+" to "+str(part_name))
    return


