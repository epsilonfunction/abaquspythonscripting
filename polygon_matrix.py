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

def matrix_centres(r,c,length):
    #Creates centres of all origin
    #Currently only square colony
    
    origin = (0.0,0.0) #must be in float for abaqus point generation to work
    output = []

    for i in range(r):
        for j in range(c):
            
            output.append(
                    
                    (float(origin[0]+i*length),float(origin[1]+j*length))

            )
    
    return output
  

def square(length,centre):  
    #takes in cartesian of origin and certain required length
    #Outputs coordinates of all points
    
    shift = length/2

    new_x_0,new_y_0 = float(centre[0]-shift),float(centre[1]-shift) #Bottom Left
    new_x_1,new_y_1 = float(centre[0]+shift),float(centre[1]+shift) #Top Right

    return [(new_x_0,new_y_0),
            (new_x_1,new_y_1)]

def hexagon(length,centre):
    #takes in cartesian of origin and certain required length
    #Outputs coordinates of all points
    pass

# print(mat_size(2,2,1))

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