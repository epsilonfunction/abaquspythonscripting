#Created by Jia Yuan on 30 July 2021
#Inputs: NONE
    #Planned: rectangle/polygon coordinates input from parameters.py 
#Outputs: Generate Parts for use in ABAQUS
#Editable: NONE

#ABAQUS Import
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

#Local Parameters Import
import poly_para as pp

def twod_rectangle(point1_input,point2_input,index): #Inputs: Tuple only; int for index/main part in string

    #Checks if inputs are tuple
    if type(point1_input) != tuple or type(point2_input) != tuple:
        raise Exception ("One of the arguments is not a cartesian point in the form of (x,y)")

    part_name=index

    if type(index) == str:
        pass
    else:
        part_name='Part-'+str(index)

    #Start of Sketch
    mdb.models['Model-1'].ConstrainedSketch(
        name='__profile__',
        sheetSize=1 #Sheetsize of 1 is dummy value
    ) 
    
    #Making Rectangle
    mdb.models['Model-1'].sketches['__profile__'].rectangle(
        point1=point1_input, #first point
        point2=point2_input  #second point
    )
    
    #Part Making
    mdb.models['Model-1'].Part(
        dimensionality=TWO_D_PLANAR,
        name=part_name,
        type=DEFORMABLE_BODY
    )
    
    #Shell (Not sure about this)
    mdb.models['Model-1'].parts[part_name].BaseShell(
        sketch=mdb.models['Model-1'].sketches['__profile__']
    )
    
    del mdb.models['Model-1'].sketches['__profile__']

# if not pp.rectangle_parameters:
#     pass

# else:    
#     counter = 0

#     for i in pp.rectangle_parameters:
        
#         twod_rectangle(
#             i[0], i[1],
#             counter
#         )

#         counter += 1


def polygon(part_name,point_input_list,two_or_three_D,*threeDpara):

    named_part=part_name

    length=len(point_input_list)
    counter=0

    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1)


    while counter < length:
        
        if counter == length-1:
            point_input1,point_input2 = point_input_list[counter],point_input_list[0]
        else:
            point_input1,point_input2 = point_input_list[counter],point_input_list[counter+1]

        mdb.models['Model-1'].sketches['__profile__'].Line(
            point1=point_input1,
            point2=point_input2
        )

        counter += 1

    height,angle = 0,0
    counter = 0
    for i in threeDpara:
        if counter == 0:
            height = i
        elif counter == 1:
            angle = i
        counter += 1

    if two_or_three_D=='two':
        mdb.models['Model-1'].Part(
            dimensionality=TWO_D_PLANAR,
            name=named_part,
            type=DEFORMABLE_BODY
        )

        mdb.models['Model-1'].parts[named_part].BaseShell(
            sketch=mdb.models['Model-1'].sketches['__profile__']
        )
    elif two_or_three_D=='three':
        mdb.models['Model-1'].Part(
            dimensionality=THREE_D,
            name=named_part,
            type=DEFORMABLE_BODY
        )
        mdb.models['Model-1'].parts[named_part].BaseSolidExtrude(
            depth=height,
            draftAngle=angle,
            sketch=mdb.models['Model-1'].sketches['__profile__']        
        )
    del mdb.models['Model-1'].sketches['__profile__']


# diamond = [
#     (-1,0),
#     (0,1),
#     (1,0),
#     (0,-1)
# ]

#twod_polygon(diamond)


#DONE: Rectangle Creation -DONE- on 4th Aug 2021 (Easy)
#DONE: Polygon Creation -DONE- on 4th Aug 2021 (Easy)
#TODO: Scaling Rectangle Creation to many variable
#TODO: Offshoring of parameters into easily editable files
#TODO (Maybe in another file): Parametric and algorithmic generation of points

