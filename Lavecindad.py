import vtk

scale = 2.5
posX=0
posY=-17
posZ=0


##CASITA

cone = vtk.vtkConeSource()
cone.SetRadius(18)
cone.SetHeight(20)
cone.SetResolution(100)
cone.Update()
cube = vtk.vtkCubeSource()
cube.SetXLength(25) 
cube.SetYLength(25)
cube.SetZLength(25)
cube.Update()
window = vtk.vtkCubeSource()
window.SetXLength(10)
window.SetYLength(15)
window.SetZLength(2)
window.Update()
door = vtk.vtkCubeSource()
door.SetXLength(15)
door.SetYLength(10)
door.SetZLength(3)
door.Update()

chapa = vtk.vtkSphereSource()
chapa.SetRadius(1)
chapa.Update()



###GRASS

grass = vtk.vtkCubeSource()
grass.SetXLength(70*scale)
grass.SetYLength(50*scale)
grass.SetZLength(5*scale)
grass.Update()

sidewalk = vtk.vtkCubeSource()
sidewalk.SetXLength(70*scale)
sidewalk.SetYLength(10*scale)
sidewalk.SetZLength(5*scale)
sidewalk.Update()

highway = vtk.vtkCubeSource()
highway.SetXLength(70*scale)
highway.SetYLength(15*scale)
highway.SetZLength(5*scale)
highway.Update()

line = vtk.vtkCubeSource()
line.SetXLength(10*scale)
line.SetYLength(5*scale)
line.SetZLength(5*scale)
line.Update()


### ARBOL

cylinder = vtk.vtkCylinderSource()
cylinder.SetRadius(4)
cylinder.SetHeight(26)
cylinder.SetResolution(50)
cylinder.Update()

Cone = vtk.vtkConeSource()
Cone.SetRadius(18)
Cone.SetHeight(20)
Cone.SetResolution(100)
Cone.Update()

cone1 = vtk.vtkConeSource()
cone1.SetRadius(18)
cone1.SetHeight(20)
cone1.SetResolution(100)
cone1.Update()

cone2 = vtk.vtkConeSource()
cone2.SetRadius(18)
cone2.SetHeight(20)
cone2.SetResolution(100)
cone2.Update()
## mapper y actors

Mapper1 = vtk.vtkPolyDataMapper()
Mapper1.SetInputData(cone.GetOutput())
Mapper2 = vtk.vtkPolyDataMapper()
Mapper2.SetInputData(cube.GetOutput())
Mapper3 = vtk.vtkPolyDataMapper()
Mapper3.SetInputData(door.GetOutput())
Mapper4 = vtk.vtkPolyDataMapper()
Mapper4.SetInputData(chapa.GetOutput())
Mapper5 = vtk.vtkPolyDataMapper()
Mapper5.SetInputData(window.GetOutput())

grass_mapper = vtk.vtkPolyDataMapper()
grass_mapper.SetInputData(grass.GetOutput())

mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(sidewalk.GetOutput())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(highway.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(line.GetOutput())



Mmapper = vtk.vtkPolyDataMapper()
Mmapper.SetInputData(cylinder.GetOutput())
Mmapper1 = vtk.vtkPolyDataMapper()
Mmapper1.SetInputData(Cone.GetOutput())
Mmapper2 = vtk.vtkPolyDataMapper()
Mmapper2.SetInputData(cone1.GetOutput())
Mmapper3 = vtk.vtkPolyDataMapper()
Mmapper3.SetInputData(cone2.GetOutput())

#actors

#actor1= cono;
Actor1 = vtk.vtkActor()
Actor1.SetMapper(Mapper1)
Actor1.GetProperty().SetColor(255/255,87/255,51/255)
Actor1.SetPosition(0,23,0)
#Actor1.RotateX(90)
Actor1.RotateZ(90)
Actor1.RotateY(-2)
#actor2= cubo;
Actor2 = vtk.vtkActor()
Actor2.SetMapper(Mapper2)
Actor2.GetProperty().SetColor(241/255,216/255,153/255)
Actor2.SetPosition(0,0,0)
Actor2.RotateY(30)

# actor3 = ventana ;
Actor3 = vtk.vtkActor()
Actor3.SetMapper(Mapper3)
Actor3.GetProperty().SetColor(96/255,189/255,226/255)
Actor3.SetPosition(-11,-1,4)
Actor3.RotateY(-60)
# actor4 = chapa ;
Actor4 = vtk.vtkActor()
Actor4.SetMapper(Mapper4)
Actor4.GetProperty().SetColor(59/255,84/255,229/255)
Actor4.SetPosition(5,-5,12)

# puerta
Actor5 = vtk.vtkActor()
Actor5.SetMapper(Mapper5)
Actor5.GetProperty().SetColor(255/255,229/255,53/255)
Actor5.SetPosition(7,-4,10)
Actor5.RotateY(30)




grass_actor = vtk.vtkActor()
grass_actor.SetMapper(grass_mapper)
grass_actor.GetProperty().SetColor(43/255,179/255,66/255)
grass_actor.SetPosition(0+posX,0+posY,0+posZ)
grass_actor.RotateX(90)


actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(102/255,102/255,99/255)
actor1.SetPosition(0+posX,0+posY,30*scale+posZ)
actor1.RotateX(90)


actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(36/255,36/255,35/255)
actor2.SetPosition(0+posX,0+posY,42.5* scale+posZ)
actor2.RotateX(90)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(1.0, 1.0, 1.0)
actor3.SetPosition(20*scale+posX,1+posY,42.5* scale+posZ)
actor3.RotateX(90)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper3)
actor5.GetProperty().SetColor(1.0, 1.0, 1.0)
actor5.SetPosition(0+posX,1+posY,42.5* scale+posZ)
actor5.RotateX(90)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper3)
actor4.GetProperty().SetColor(1.0, 1.0, 1.0)
actor4.SetPosition(-20*scale+posX,1+posY,42.5*scale+posZ)
actor4.RotateX(90)



Aactor = vtk.vtkActor()
Aactor.SetMapper(Mmapper)
Aactor.GetProperty().SetColor(1.0, 0.6, 0.0)
Aactor.RotateX(10.0)
Aactor.SetPosition(0+40,0,0)

Aactor1 = vtk.vtkActor()
Aactor1.SetMapper(Mmapper1)
Aactor1.GetProperty().SetColor(0.0, 0.70, 0.0)
Aactor1.SetPosition(0+40,23,0)
Aactor1.RotateZ(90)
Aactor1.RotateY(-2)

Aactor2 = vtk.vtkActor()
Aactor2.SetMapper(Mmapper2)
Aactor2.GetProperty().SetColor(0.0, 0.75, 0.0)
Aactor2.SetPosition(0+40,20,0)
Aactor2.RotateZ(90)
Aactor2.RotateY(-5)

Aactor3 = vtk.vtkActor()
Aactor3.SetMapper(Mmapper3)
Aactor3.GetProperty().SetColor(0.0, 0.75, 0.0)
Aactor3.SetPosition(0+40,17,0)
Aactor3.RotateZ(90)
Aactor3.RotateY(-5)





# add actors to renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(Actor1)
renderer.AddActor(Actor2)
renderer.AddActor(Actor3)
renderer.AddActor(Actor4)
renderer.AddActor(Actor5)
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)
renderer.AddActor(grass_actor)

renderer.AddActor(Aactor)
renderer.AddActor(Aactor1)
renderer.AddActor(Aactor2)
renderer.AddActor(Aactor3)
#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(400, 400)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
