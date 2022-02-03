# Copy Model
mdb.Model(name='Model-2',objectToCopy=mdb.models['Model-1'])
# mdb.Model(name=new_name,objectToCopy=old_name) smth liddat

#mdb.models['Model-2'].parts['final'].deleteMesh()
# Must delete before remeshing with new conditions i guess

# Regenerating instance upon new meshing
mdb.models['Model-2'].rootAssembly.regenerate()

