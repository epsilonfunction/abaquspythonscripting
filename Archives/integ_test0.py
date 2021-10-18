# -*- coding: mbcs -*-
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
mdb.models['Model-1'].Material(name='Material-0')
mdb.models['Model-1'].materials['Material-0'].Elastic(table=((1000000, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-0', name=
    'Section-0', thickness=None)
mdb.models['Model-1'].Material(name='Material-1')
mdb.models['Model-1'].materials['Material-1'].Elastic(table=((100000, 0.3), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-1', name=
    'Section-1', thickness=None)
mdb.models['Model-1'].Material(name='Material-2')
mdb.models['Model-1'].materials['Material-2'].Elastic(table=((500000, 0.01), ))
mdb.models['Model-1'].HomogeneousSolidSection(material='Material-2', name=
    'Section-2', thickness=None)
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1)
mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-0.5, -0.5), 
    point2=(0.5, 0.5))
mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Main0', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['Main0'].BaseShell(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Part(name='Part-0', objectToCopy=
    mdb.models['Model-1'].parts['Main0'])
mdb.models['Model-1'].Part(name='Part-1', objectToCopy=
    mdb.models['Model-1'].parts['Main0'])
mdb.models['Model-1'].Part(name='Part-2', objectToCopy=
    mdb.models['Model-1'].parts['Main0'])
mdb.models['Model-1'].parts['Main0'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models['Model-1'].parts['Main0'].faces.findAt(((-0.166667, 
    -0.166667, 0.0), (0.0, 0.0, 1.0)), )), sectionName='Section-0', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Main0'].setMeshControls(elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['Main0'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), technique=STRUCTURED)
mdb.models['Model-1'].parts['Main0'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6M, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Main0'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), ))
mdb.models['Model-1'].parts['Main0'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Main0'].generateMesh()
mdb.models['Model-1'].parts['Part-0'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models['Model-1'].parts['Part-0'].faces.findAt(((-0.166667, 
    -0.166667, 0.0), (0.0, 0.0, 1.0)), )), sectionName='Section-0', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-0'].setMeshControls(elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['Part-0'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), technique=STRUCTURED)
mdb.models['Model-1'].parts['Part-0'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6M, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-0'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), ))
mdb.models['Model-1'].parts['Part-0'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-0'].generateMesh()
mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models['Model-1'].parts['Part-1'].faces.findAt(((-0.166667, 
    -0.166667, 0.0), (0.0, 0.0, 1.0)), )), sectionName='Section-1', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-1'].setMeshControls(elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['Part-1'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), technique=STRUCTURED)
mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6M, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-1'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), ))
mdb.models['Model-1'].parts['Part-1'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-1'].generateMesh()
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    faces=mdb.models['Model-1'].parts['Part-2'].faces.findAt(((-0.166667, 
    -0.166667, 0.0), (0.0, 0.0, 1.0)), )), sectionName='Section-2', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(elemShape=QUAD, regions=
    mdb.models['Model-1'].parts['Part-2'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), technique=STRUCTURED)
mdb.models['Model-1'].parts['Part-2'].setElementType(elemTypes=(ElemType(
    elemCode=CPS8R, elemLibrary=STANDARD), ElemType(elemCode=CPS6M, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-2'].faces.findAt(((-0.166667, -0.166667, 
    0.0), )), ))
mdb.models['Model-1'].parts['Part-2'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=0.5)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Main0-1', part=
    mdb.models['Model-1'].parts['Main0'])
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
    part=mdb.models['Model-1'].parts['Part-1'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Part-1-1', ), 
    vector=(1.0, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['Model-1'].rootAssembly.instances['Main0-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1']), 
    keepIntersections=ON, name='Main1', originalInstances=DELETE)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-2-1', 
    part=mdb.models['Model-1'].parts['Part-2'])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Part-2-1', ), 
    vector=(2.0, 0.0, 0.0))
del mdb.models['Model-1'].parts['Main0']
mdb.models['Model-1'].rootAssembly.InstanceFromBooleanMerge(domain=GEOMETRY, 
    instances=(mdb.models['Model-1'].rootAssembly.instances['Main1-1'], 
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1']), 
    keepIntersections=ON, name='Main0', originalInstances=DELETE)
# Save by jiayuan on 2021_08_12-16.35.49; build 2021 2020_03_06-22.50.37 167380
