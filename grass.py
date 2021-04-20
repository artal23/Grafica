#!/usr/bin/env python
# coding: utf-8

# In[1]:

import vtk

# In[36]:
#Some parameters to vary the proportion and position
scale = 1
posX=0
posY=0
posZ=0
# source
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

# mapper
grass_mapper = vtk.vtkPolyDataMapper()
grass_mapper.SetInputData(grass.GetOutput())

mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(sidewalk.GetOutput())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(highway.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(line.GetOutput())

#actor
grass_actor = vtk.vtkActor()
grass_actor.SetMapper(grass_mapper)
grass_actor.GetProperty().SetColor(43/255,179/255,66/255)
grass_actor.SetPosition(0+posX,0+posY,0+posZ)

actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(102/255,102/255,99/255)
actor1.SetPosition(0+posX,30+posY,0+posZ)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(36/255,36/255,35/255)
actor2.SetPosition(0+posX,42.5+posY,0+posZ)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(1.0, 1.0, 1.0)
actor3.SetPosition(20+posX,42.5+posY,1+posZ)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper3)
actor5.GetProperty().SetColor(1.0, 1.0, 1.0)
actor5.SetPosition(0+posX,42.5+posY,1+posZ)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper3)
actor4.GetProperty().SetColor(1.0, 1.0, 1.0)
actor4.SetPosition(-20+posX,42.5+posY,1+posZ)


#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(grass_actor)
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
