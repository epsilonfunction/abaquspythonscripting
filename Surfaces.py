# from part import *
# from material import *
# from section import *
# from assembly import *
# from step import *
# from interaction import *
# from load import *
# from mesh import *
# from optimization import *
# from job import *
# from sketch import *
# from visualization import *
# from connectorBehavior import *
print("working")
from math import cos,sin,radians

def left_surf_grp(rve_size,lam_semi_length,lam_semi_height):

    x,y,z = rve_size[0]/2.0,lam_semi_height/2.0,0.0
    dx = 0.2
    roots=(x,y,z)
    
    positive_half=[]

    limits=[rve_size[0]/2,rve_size[2],rve_size[1]/2] #x,y,z convention

    stem = []
    while z <= limits[2]:

        bottom_face=(x,y,z-dx)
        stem.append(bottom_face)
        # positive_half.append(bottom_face)

        z += lam_semi_length*1.50 

    last = (x,y,limits[2]-dx)
    stem.append(last)

    while y <= limits[1]:

        for i in stem:
            face=(i[0],y,i[2])
            positive_half.append(face)

        y+=lam_semi_height
 

    all_pointsofface = []

    for i in positive_half:
        if i[2] == 0.0:
            pass
        else:
            j = (i[0],i[1],-1.0*i[2])
            all_pointsofface.append(j)
        all_pointsofface.append(i)

    last = []
    for i in stem:
        new_i_1=limits[1]-dx
        to_add=(i[0],new_i_1,i[2])
        last.append(to_add)

    return all_pointsofface+last

def right_surf_grp(rve_size,lam_semi_length,lam_semi_height):

    all_lefts=left_surf_grp(rve_size,lam_semi_length,lam_semi_height)

    mirrored_to_right=[]

    for i in all_lefts:
        mirrored = (-1*i[0],i[1],i[2])
        mirrored_to_right.append(mirrored)
    
    return mirrored_to_right

             

def top_surf(rve_size,lam_semi_width):
    
    x,y,z = 0.0,rve_size[2],0.0
    roots=(x,y,z)
    quadrants=[roots]

    limits=[rve_size[0]/2, rve_size[2],rve_size[1]/2] #in x,y,z format
    
    dx=0.2
    x_search=lam_semi_width*2.0*cos(radians(30.0))
    
    x+=lam_semi_width*cos(radians(30.0))
    
    stem=[]
    while x <= limits[0]:
        
        to_add = (x+dx,y,z)
        stem.append(to_add)
        quadrants.append(to_add)

        x+=x_search
    # print(stem)

    z_maj_srh,z_min_srh=3.0*lam_semi_width,2.0*lam_semi_width
    counter=1
    while z <= limits[2]:

        # majleaf=[]
        for i in stem:
            component = list(i)
            component[2]+=z_maj_srh*counter
            component = tuple(component)
            # majleaf.append(i)
            quadrants.append(component)

        z+=z_maj_srh
        counter+=1

    shift=(lam_semi_width*cos(radians(30.0)),0.0, lam_semi_width*sin(radians(30.0)))
    more_points=[]
    for i in quadrants:
        new_points=[]
        for j in range(3):
            new_points+=[i[j]+shift[j]]
        if new_points[0]<limits[0] and new_points[2]<limits[2]:
            new_points[2]+=dx
            # new_points.append(z)
            new_points = tuple(new_points)
            
            more_points.append(new_points)
    
    quadrants = quadrants+more_points
    prelimit=[p for p in limits]
    print(prelimit)
    prelimit[0]-=dx
    prelimit[2] -= dx
    quadrants.append(tuple(prelimit))

    halves=[]
    for j in quadrants:
        if j[2] == 0.0:
            halves.append(j)
        else:
            j_prime = list(j)
            j_prime[2] *= -1
            j_prime=tuple(j_prime)
            halves.append(j),halves.append(j_prime)

    all_points=[]
    for k in halves:
        if k[0] == 0.0:
            all_points.append(k)
        else:
            k_prime = list(k)
            k_prime[0] *= -1
            k_prime=tuple(k_prime)
            all_points.append(k),all_points.append(k_prime)


    return all_points

def bot_surf(lam_height):

    bottom=(0.0,-1*lam_height,0.0)

    return mirrored_to_right

def front_surf_grp(rve_size,lam_semi_length,lam_semi_height):
    
    x,y,z = 0.0,lam_semi_height/2.0,rve_size[1]/2.0
    dx = 0.2
    roots=(x,y,z)

    limits=[rve_size[0]/2, rve_size[2],rve_size[1]/2] #in x,y,z format
    
    stem=[]

    while x <= limits[0]:

        bottom_face = (x-dx,y,z)
        stem.append(bottom_face)

        x += lam_semi_length*cos(radians(30))
    last = (limits[0]-dx,y,z)
    stem.append(last)
    positive_half=[]
    while y <= limits[1]:

        for i in stem:
            face=(i[0],y,i[2])
            positive_half.append(face)
        

        y+=lam_semi_height

    all_pointsofface = []

    for i in positive_half:
        if i[1] == 0.0:
            pass
        else:
            j = (-1.0*i[0],i[1],i[2])
            all_pointsofface.append(j)
        all_pointsofface.append(i)
    
    last=[]
    for i in stem:
        new_i_1=limits[1]-dx
        to_add=(i[0],new_i_1,i[2])
        last.append(to_add)

    return all_pointsofface+last

def back_surf_grp(rve_size,lam_semi_length,lam_semi_height):

    front=front_surf_grp(rve_size,lam_semi_length,lam_semi_height)

    back = []

    for i in front:
        to_add = (i[0],i[1],-1.0*i[2])
        back.append(to_add)

    return back


#test_rve=(3897.0,1125.0,150.0)
# test_rve=(779.4,450.0,150.0)
# test_length=150.0
# test_height=25.0
# print((top_surf(test_rve,test_length)))

# print(front_surf_grp(test_rve,test_length,test_height))