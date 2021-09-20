def hexa_3_findsurr(coord,length):
    vector=(0.0,length*3)
    output=[]
    for i in range(6):
        translation_vector=vector_rotate(i*60.0, vector)
        new_centre=(
            float(round(centre[0]+translation_vector[0],5)),
            float(round(centre[1]+translation_vector[1],5))
        )
        output.append(new_centre)
    return output
def hexa_all(centre,length,maxdist,color):
    output = []
    search_dist=maxdist+2*length
    if color == 3:
        for i in range(colour):
            if i == 0:
                search_centre=centre
            elif i ==1:
                search_centre=centre+(0.0,length*0.86603)
            elif i==2:
                search_centre=centre+(0.0,length*0.86603*-1.0)
            
            yet_to_search.append(search_centre)
            to_return.append(search_centre)

            while len(yet_to_search)>0:
                check=yet_to_search.pop(0)
                
                check_list=hexa_3_findsurr(check,length)
                for j in check_list:
                    if j in to_return:
                        pass
                    else:
                        dist=(j[0]-centre[0])**2+(j[1]-centre[1])**2
                        if dist <= search_dist:
                            yet_to_search.append(j)
                            to_return.append(k)
            output.append(to_return)
    return output

print(hexa_all((0.0,0.0),150.0,1000.0,3))