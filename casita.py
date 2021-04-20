import vtk
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

## mapper y actors

mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(cone.GetOutput())
mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(cube.GetOutput())
mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(door.GetOutput())
mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputData(chapa.GetOutput())
mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputData(window.GetOutput())

#actors

#actor1= cono;
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(255/255,87/255,51/255)
actor1.SetPosition(0,23,0)
#actor1.RotateX(90)
actor1.RotateZ(90)
actor1.RotateY(-2)
#actor2= cubo;
actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(241/255,216/255,153/255)
actor2.SetPosition(0,0,0)
actor2.RotateY(30)

# actor3 = ventana ;
actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(96/255,189/255,226/255)
actor3.SetPosition(-11,-1,4)
actor3.RotateY(-60)
# actor4 = chapa ;
actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor4.GetProperty().SetColor(59/255,84/255,229/255)
actor4.SetPosition(5,-5,12)

# puerta
actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor5.GetProperty().SetColor(255/255,229/255,53/255)
actor5.SetPosition(7,-4,10)
actor5.RotateY(30)

# add actors to renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)

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
