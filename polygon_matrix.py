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

def deg_to_rad(degrees):
    radians = (degrees/180)*math.pi
    return radians

def hexagon(length,centre,angle):
    #angle(in degrees): angle of tilt of first point wrt to centre
    radians = [angle,60,60]
    for i in range(3):
        radians[i]=deg_to_rad(radians[i])

    output = []

    translation_vector_0 = [length,0]
    rotation_vector=[]

    for j in radians:
        rotation_vector.append(
            (
                (math.cos(j),-1*math.sin(j)),
                (math.sin(j),   math.cos(j))
            )
        )   
    
    translation_vector_1 = np.matmul(
        rotation_vector[0],translation_vector_0
    )
    
    point_1=(round(centre[0]+translation_vector_1[0],5),round(centre[1]+translation_vector_1[1],5))
    output.append(point_1)
    translation_vector_2 = np.matmul(
        rotation_vector[1],translation_vector_1
    )
    for k in range(5):
        translation_vector_2 = np.matmul(
            rotation_vector[2],translation_vector_2
        )
        point_1=(
            round(point_1[0]+translation_vector_2[0],5),round(point_1[1]+translation_vector_2[1],5)
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