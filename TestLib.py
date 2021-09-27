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

orientation_dict={
 'Standard': [[3.749399456654644e-33, -6.123233995736766e-17, 1.0], [1.0, 0.0, 1.0]],
 'Gamma-I-M': [[-0.7071, 0.57737, -0.40824], [-0.70709, 1.15471, 0.40826]], 
 'Gamma-I-T': [[0.7071, 0.57737, 0.40824], [0.70709, 1.15471, -0.40826]], 
 'Gamma-II-M': [[0.0, 0.57737, 0.81648], [0.70711, 1.15471, 0.40822]], 
 'Gamma-II-T': [[0.0, 0.57737, -0.81648], [-0.70711, 1.15471, -0.40822]], 
 'Gamma-III-M': [[0.7071, 0.57737, -0.40824], [-2e-05, 1.15471, -0.81648]], 
 'Gamma-III-T': [[-0.7071, 0.57737, 0.40824], [2e-05, 1.15471, 0.81648]]

}

# mdb.models['Model-1'].materials['Gamma_Phase'].Elastic(
#     table=(
#         (190000000000.0, 105000000000.0, 190000000000.0,
#         90000000000.0, 90000000000.0,185000000000.0,
#         120000000000.0, 120000000000.0, 50000000000.0),
#     ),
#     type=ORTHOTROPIC
# )
def fn():


    mdb.models['Model-1'].Material(name = "alpha2")
    mdb.models['Model-1'].materials['alpha2'].Elastic(
        table=(
                (221.0,71.0, 221.0,
                85.0, 85.0, 221.0,
                69.0, 69.0, 75.0), 
        ),        
        type=ORTHOTROPIC
    )
    mdb.models['Model-1'].HomogeneousSolidSection(material='alpha2', name=
        'alpha2', thickness=None)


    mdb.models['Model-1'].Material(name = "gamma")
    mdb.models['Model-1'].materials['gamma'].Elastic(
        table=(
            (190.0, 105.0, 190.0,
            90.0, 90.0, 185.0, 
            120.0, 120.0, 50.0), 
        ),
        type=ORTHOTROPIC
    )
    mdb.models['Model-1'].HomogeneousSolidSection(material='gamma', name=
        'gamma', thickness=None)

# ______________________________________________________________________ #
    mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Standard', origin=(0.0, 0.0, 0.0), point1=(0.0, 0.0, 1.0), 
        point2=(1.0, 0.0, 1.0))
    mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Gamma-I-M', origin=(0.0, 0.0, 0.0), point1=(-0.7071, 
        0.57737, -0.40824), point2=(-0.70709, 1.15471, 0.40826))
    mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Gamma-I-T', origin=(0.0, 0.0, 0.0), point1=(0.7071, 
        0.57737, 0.40824), point2=(0.70709, 1.15471, -0.40826))
    mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Gamma-II-M', origin=(0.0, 0.0, 0.0), point1=(0.0, 0.57737, 
        0.81648), point2=(0.70711, 1.15471, 0.40822))
    mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Gamma-II-T', origin=(0.0, 0.0, 0.0), point1=(0.0, 0.57737, 
        -0.81648), point2=(-0.70711, 1.15471, -0.40822))
    mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Gamma-III-M', origin=(0.0, 0.0, 0.0), point1=(0.7071, 
        0.57737, -0.40824), point2=(-2e-05, 1.15471, -0.81648))
    mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(coordSysType=
        CARTESIAN, name='Gamma-III-T', origin=(0.0, 0.0, 0.0), point1=(-0.7071, 
        0.57737, 0.40824), point2=(2e-05, 1.15471, 0.81648))

    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['Alpha_2'], sectionName=
        'alpha2', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['Gamma-I-M'], sectionName=
        'gamma', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['Gamma-I-T'], sectionName=
        'gamma', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['Gamma-II-M'], sectionName=
        'gamma', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['Gamma-II-T'], sectionName=
        'gamma', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['Gamma-III-M'], sectionName=
        'gamma', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['Gamma-III-T'], sectionName=
        'gamma', thicknessAssignment=FROM_SECTION)
        
    mdb.models['Model-1'].parts['final'].MaterialOrientation(
        additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
        , axis=AXIS_3, fieldName='', localCsys=
        mdb.models['Model-1'].parts['final'].datums[9], orientationType=SYSTEM, 
        region=mdb.models['Model-1'].parts['final'].sets['Gamma-I-M'], 
        stackDirection=STACK_ORIENTATION)

    return


# mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(
#     coordSysType=CARTESIAN, 
#     name='Standard', 
#     origin=(0.0, 0.0, 0.0), 
#     point1=(0.0, 0.0, 1.0), 
#     point2=(1.0, 0.0, 1.0)
# )
# mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(
#     coordSysType=CARTESIAN, 
#     name='Gamma-I-M', 
#     origin=(0.0, 0.0, 0.0), 
#     point1=(-0.7071,0.57737, -0.40824), 
#     point2=(-0.70709, 1.15471, 0.40826)
# )

# mdb.models['Model-1'].parts['final'].DatumCsysByThreePoints(
#     coordSysType=CARTESIAN, 
#     name='Gamma-I-T', 
#     origin=(0.0, 0.0, 0.0), 
#     point1=(0.7071,0.57737, 0.40824),
#     point2=(0.70709, 1.15471, -0.40826)
# )