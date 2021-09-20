import polygon_creation as polygen
# import poly_para as pp

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


import numpy as np
import math
#import polygon_creation as poly_gen
# class polygon_matrix(self):
#     self.polygon_type=None #string?
#     self.size = None #tuple
#     self.centers = [] #list
#     self.polygon_size = None #int

#     def set_size(r,c):
#         self.size=(r,c)

#     def generate_centers():
#         for r in range(self.size[0]):
#             add_row = []
#             for c in range(self.size[1]):
#                 pass

def deg_to_rad(degrees):
    radians = (float(degrees)/float(180))*math.pi
    return radians

def vector_rotate(angle,vector):
    #angle in degrees| int
    #vector in array-like| list/tuple
    radians = deg_to_rad(angle)
    rotation_matrix = (
        (math.cos(radians),-1*math.sin(radians)),
        (math.sin(radians),   math.cos(radians))
    )
    new_vector = np.matmul(rotation_matrix,vector)
    return new_vector

def matrix_centres(r,c,length,polygon_type):
    #Creates centres of all instances
    #Currently only square colony
    
    origin = (0.0,0.0) #must be in float for abaqus point generation to work
    output = []
    output.append(origin)

    if polygon_type=='square':

        for i in range(r):
            for j in range(c):
            
                output.append(
                    
                    (float(origin[0]+i*length),float(origin[1]+j*length))

                )
    
        return output
    
    elif polygon_type == 'hexagon': #two depth deep of all centres
        vector = (0,0.86603*length*2)
        counter = 1

        def findallhexagoncenter(centre,vector):
            vector_list = []
            for i in range(6):
                translation_vector=vector_rotate(30+i*60, vector)
                new_centre=(
                    float(round(centre[0]+translation_vector[0],5)),
                    float(round(centre[1]+translation_vector[1],5))
                )
                vector_list.append(new_centre)
            return vector_list
        def elim_dupes(arr):
            output = list(dict.fromkeys(arr))
            return output

        # first_depth=findallhexagoncenter(origin,vector)
        # output.append(first_depth)
        
        output.append([origin])
        prev_depth_1=[]
        prev_depth_2=[origin]
        while counter <= r:
            curr_depth = []
            if counter == 1:
                curr_depth=findallhexagoncenter(origin,vector)
        
                output.append(curr_depth)
                prev_depth_1=curr_depth

            else:
                for i in prev_depth_1:
                    curr_depth=curr_depth+findallhexagoncenter(i,vector)

                curr_depth=elim_dupes(curr_depth)

                for j in curr_depth:
                    if j in prev_depth_1 or prev_depth_2:
                        curr_depth.remove(j)
                
                output.append(curr_depth)
                prev_depth_2=prev_depth_1
                prev_depth_1=curr_depth

            counter += 1
        #             for j in check_list:
        #                 for k in j:
        #                     if k not in output[counter-1] or not (0.0, 0.0):
        #                         to_add.append(k)
        #         else:
        #             for j in check_list:
        #                 if j not in output[counter-1] or output[counter-2]:
        #                     to_add.append(j)
        #         output.append(to_add)

        #       counter+=1
    # def flatten(l): #copied from http://rightfootin.blogspot.com/2006/09/more-on-python-flatten.html
    #     out = []
    #     for item in l:
    #         if isinstance(item, (list)):
    #             out.extend(flatten(item))
    #         else:
    #             out.append(item)
    #     return out
    # a = flatten(output)
    # a = list(dict.fromkeys(a)) #remove duplicates

    return output
    
def square(length,centre):  
    #takes in cartesian of origin and length of square
    #Outputs coordinates of opposing ends in square for sketching
    
    shift = length/2

    new_x_0,new_y_0 = float(centre[0]-shift),float(centre[1]-shift) #Bottom Left
    new_x_1,new_y_1 = float(centre[0]+shift),float(centre[1]+shift) #Top Right

    return [(new_x_0,new_y_0),
            (new_x_1,new_y_1)]

def rectangle(width,height,centre):
    #takes in cartesian coordinates of origin and height and width of rectangle
    #Outputs coordinates of opposing ends in square for sketching

    shift_x,shift_y=width/2,height/2

    new_x_0,new_y_0 = float(centre[0]-shift_x),float(centre[1]-shift_y) #Bottom Left
    new_x_1,new_y_1 = float(centre[0]+shift_x),float(centre[1]+shift_y) #Top Right



def hexagon(length,centre):
    #Rotation to be done after creation
    #Creates points for sketching of hexagon
    output = []

    translation_vector_0 = [0.0,length]
    rotation_vector=[]
    
    point_1=(round(centre[0]+translation_vector_0[0],5),round(centre[1]+translation_vector_0[1],5))
    output.append(point_1)

    translation_vector_1 = vector_rotate(60,translation_vector_0)

    for k in range(5):
        translation_vector_1 = vector_rotate(60,translation_vector_1)
        point_1=(
            round(point_1[0]+translation_vector_1[0],5),
            round(point_1[1]+translation_vector_1[1],5)
        )
    
        output.append(point_1)
    
    return output

def sketch_add(points_list):
    
    output = []

    for i in range(len(points_list)):
        
        coordinates = points_list[i]
            
        if i == 0:
            part_name = "main_part"
        else:
            part_name = i

        polygen.twod_rectangle(
            coordinates[0],coordinates[1],
            part_name
        )

        output.append(part_name)
    
    return output
    
    pass

def hexa_3_findsurr(coord,length):
    vector=(0.0,length*3)
    output=[]
    for i in range(6):
        translation_vector=vector_rotate(i*60.0, vector)
        new_centre=(
            float(round(coord[0]+translation_vector[0],5)),
            float(round(coord[1]+translation_vector[1],5))
        )
        output.append(new_centre)
    return output
def hexa_all(centre,length,maxdist,color):
    output = []
    search_dist=maxdist+2*length
    print(search_dist)
    if color == 3:
        for i in range(color):
            if i == 0:
                search_centre=centre
            elif i ==1:
                search_centre=(centre[0]+length*2*0.86603,centre[1]+0.0)
            elif i==2:
                search_centre=(centre[0]-length*2*0.86603,centre[1]+0.0)
            
            yet_to_search,to_return=[],[]
            yet_to_search.append(search_centre)
            to_return.append(search_centre)

            while len(yet_to_search)>0:
                check=yet_to_search.pop(0)
                
                check_list=hexa_3_findsurr(check,length)
                for j in check_list:
                    if j in to_return:
                        pass
                    else:
                        dist=math.sqrt((j[0]-centre[0])**2+(j[1]-centre[1])**2)
                        if dist <= search_dist:
                            yet_to_search.append(j)
                            to_return.append(j)
            output.append(to_return)
    return output
