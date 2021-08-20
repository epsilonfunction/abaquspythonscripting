#Created by Jia Yuan on 30 July 2021
#Inputs: Material Parameters from Parameters.py
#Outputs: Generate Materials, ready for use in ABAQUS
#Editable: NONE

from material import *
#from Parameters import material_parameters as mp
#List of Materials to be implemented here.
#Each Material is a tuple represented as (Young's Modulus,Poisson Ratio) 

def material_input(mat_name,E,v): #Takes in material's name, Young's Modulus(E), and Poisson Ratio

    #Adding Instance of material with the convention of: Material-{Index}
    mdb.models['Model-1'].Material(
        name = mat_name
    )

    #Adding material parameters to material instance
    mdb.models['Model-1'].materials[mat_name].Elastic(
        table=((E,v), )
    )

    #Adding name
    return

def sectioning (mat_name,section_name):
    mdb.models['Model-1'].HomogeneousSolidSection(
            material=mat_name,
            name=section_name,
            thickness=None
        )
    
    # print(section_name+"has been added")

#Outputs list of material
def generate_materials(lst): #lst is list of material
    #Input: List of material properties
        #Format: [Young's Modulus, Poisson Ratio,Material Name Placeholder,Section Name Placeholder] 

    #Output: List of material properties + assigned name
        #Format: [Young's Modulus, Poisson Ratio,Material Name,Section Name Placeholder]

    #Output of this function
    output = lst 

    for i in range(len(lst)): 
    
    #Generates material name and append to list for easy calling.
        material_name = 'Material-'+str(i)
        output[i][2] = material_name

        section_name='Section-'+str(i)
        output[i][3] = section_name

    #Inputs Material parameters into abaqus
        material_input(
            material_name,
            lst[i][0],
            lst[i][1]
        )

        # print(section_name+"has not been added")

    #Sections Material parameters
        sectioning(
            material_name,
            section_name
        )

    #Returns a list of materials used.
    return output


#DONE: Add in Material Sectioning (if deemed appropriate) -DONE- on 30th July 2021.
#DONE: Add material name (i.e 'Material-1') into material_list, and make it callable to others. -DONE- on 30th July 2021.
#TODO: Allow Custom naming (e.g. such as steel, Ti3Al, TiAl) to remain untouched

#EDITS: Separated Material Parameters into new file | Parameters are to be imported
#EDITS (4th Aug 2021): Renamed from materials.py to material_creation.py | Avoid clashing with materials import from abaqus
#Section Creation will import parameters from this file.
#EDITS(10th Aug 2021): Reworked into general method that does not take directly from parameters.py
