
def g():
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
        mdb.models['Model-1'].parts['final'].sets['gamma-I-M'], sectionName=
        'gamma_sec', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['gamma-I-T'], sectionName=
        'gamma_sec', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['gamma-II-M'], sectionName=
        'gamma_sec', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['gamma-II-T'], sectionName=
        'gamma_sec', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['gamma-III-M'], sectionName=
        'gamma_sec', thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['final'].SectionAssignment(offset=0.0, offsetField=
        '', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['final'].sets['gamma-III-T'], sectionName=
        'gamma_sec', thicknessAssignment=FROM_SECTION)