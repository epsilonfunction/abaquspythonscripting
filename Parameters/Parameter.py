#Here Goes Material instanceList
gamma=( 
    190000000000.0,105000000000.0, 190000000000.0,
    90000000000.0, 90000000000.0,185000000000.0,
    120000000000.0, 120000000000.0, 50000000000.0
)

alpha2=(
    190000000000.0,105000000000.0, 190000000000.0,
    90000000000.0, 90000000000.0,185000000000.0,
    120000000000.0, 120000000000.0, 50000000000.0
)
#Each material to be added as a list in entry: [Young's Modulus, Poisson Ratio, Material Name, Section Name]
material_parameters = [
    [gamma,'Gamma','section_name_placeholder'],
    [alpha2,'Alpha_2','section_name_placeholder'],
]
gamma_variant=[
    ("Gamma-I-M",[]),
    ("Gamma-I-T",[]),
    ("Gamma-II-M",[]),
    ("Gamma-II-T",[]),
    ("Gamma-III-M",[]),
    ("Gamma-III-T",[])
]
alpha_variant=[
    ("Alpha_2",[0])
]
#CREATED (31st July 2021): Added material_parameters; an array of materials with Young's Modulus and Poisson Ratio

