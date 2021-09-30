import numpy as np
import math

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

def hexa_3_findsurr(coord,length):

    vector=(0.0,length*3)
    output=[]
    for i in range(6):
        translation_vector=vector_rotate(i*60.0, vector)
        x_n,y_n=float(coord[0]+translation_vector[0]),float(coord[1]+translation_vector[1])

        new_x,new_y=float("{:.2f}".format(x_n)),float("{:.2f}".format(y_n))
        
        new_centre=(
            new_x,new_y
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


print(hexa_all((0.0,0.0),150.0,1000.0,3))