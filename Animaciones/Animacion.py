import vtk
import numpy as np
import math

class MySphere:
    def __init__(self, pos, radius,x,y,z,textura):
        self.pos = pos
        self.radius = radius
        self.velocity = [x,y,z ]# la esfera cae, por eso tiene una velocida hacia abajo  6,0,-4
        self.last_velocity = [1,0,1]
        self.textura = textura
        self.actor = None

class MyFloor:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height
        #self.textura = textura
        self.velocity = np.array([0,0,0])
        self.actor = None

class MyWall:
    def __init__(self, pos, height, textura ):
        self.pos = pos
        self.height = height
        self.velocity = np.array([0,0,0])
        self.textura = textura
        self.actor = None

reader = vtk.vtkJPEGReader()
reader.SetFileName("1.jpg")

texture = vtk.vtkTexture()
texture.SetInputConnection(reader.GetOutputPort())


sphere = MySphere([0,4,0], 4 ,3 , 0,0 , texture)







readerdos = vtk.vtkJPEGReader()
readerdos.SetFileName("dos.jpg")

texturedos = vtk.vtkTexture()
texturedos.SetInputConnection(readerdos.GetOutputPort())


sphere2= MySphere([15,4,0], 6 , -3 ,0 ,0 , texturedos)

'''
readerFloor = vtk.vtkJPEGReader()
readerFloor.SetFileName("piso4.jpg")

textureFloor = vtk.vtkTexture()
textureFloor.SetInputConnection(readerFloor.GetOutputPort())
'''


floor = MyFloor([0,0,0], 1)

readerWall = vtk.vtkJPEGReader()
readerWall.SetFileName("bordes.jpg")

textureWall = vtk.vtkTexture()
textureWall.SetInputConnection(readerWall.GetOutputPort())


wallheight = 4
wallup = MyWall([0,2,200], wallheight,textureWall)
walldown = MyWall([0,2,-200], wallheight,textureWall)
wallleft = MyWall([200,2,0], wallheight,textureWall)
wallright = MyWall([-200,2,0], wallheight,textureWall)

time = 0
g = 9
def set_initial_position():
    sphere_actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])
    sphere_actor2.SetPosition(sphere2.pos[0], sphere2.pos[1], sphere2.pos[2])

    floor_actor.SetPosition(floor.pos[0], floor.pos[1], floor.pos[2])
    wallup_actor.SetPosition(wallup.pos[0], wallup.pos[1], wallup.pos[2])
    walldown_actor.SetPosition(walldown.pos[0], walldown.pos[1], walldown.pos[2])
    wallleft_actor.SetPosition(wallleft.pos[0], wallleft.pos[1], wallleft.pos[2])
    wallright_actor.SetPosition(wallright.pos[0], wallright.pos[1], wallright.pos[2])

def reduc():
    sphere.velocity[0] = sphere.velocity[0] * 0.95
    sphere.velocity[2] = sphere.velocity[2] * 0.95


def SpeedControler(ball):
    ball.pos[0] = ball.pos[0] + ball.velocity[0]
    ball.pos[2] = ball.pos[2] + ball.velocity[2]
    # distancia = velocidad * tiempo
    # new_position =  old_position + velocidad * tiempo
    ball.velocity[0] = ball.velocity[0]*0.999
    ball.velocity[2] = ball.velocity[2] * 0.999
    ball.last_velocity[0] = ball.velocity[0]
    ball.last_velocity[2] = ball.velocity[2]

    if((abs(ball.velocity[0]) or abs(ball.velocity[2])) < 0.2):
        ball.velocity[0] = 0
        ball.velocity[2] = 0

def ColisionWall(ball):

    if (ball.pos[2] - ball.radius < -200):
        ball.velocity[2] = (ball.velocity[2] * -1)
        ball.pos[0] = ball.pos[0] + ball.velocity[0]
        ball.pos[2] = ball.pos[2] + ball.velocity[2]
        reduc()
    if (ball.pos[2] - ball.radius > 200):
        ball.velocity[2] = (ball.velocity[2] * -1)
        ball.pos[0] = ball.pos[0] + ball.velocity[0]
        ball.pos[2] = ball.pos[2] + ball.velocity[2]
        reduc()
    if (ball.pos[0] - ball.radius < -200):
        ball.velocity[0] = (ball.velocity[0] * -1)
        ball.pos[0] = ball.pos[0] + ball.velocity[0]
        ball.pos[2] = ball.pos[2] + ball.velocity[2]
        reduc()
    if (ball.pos[0] - ball.radius > 200):
        ball.velocity[0] = (ball.velocity[0] * -1)
        ball.pos[0] = ball.pos[0] + ball.velocity[0]
        ball.pos[2] = ball.pos[2] + ball.velocity[2]
        reduc()

def distanceBalls(ball1,ball2):
    result = ( (ball2.pos[0]-ball1.pos[0]) * (ball2.pos[0]-ball1.pos[0]) ) +  ( (ball2.pos[2]-ball1.pos[2])* (ball2.pos[2]-ball1.pos[2]) )
    return result

def detectColision(ball1 , ball2):
    rSquared = ball1.radius +ball2.radius 
    
    if (distanceBalls(ball1,ball2)<rSquared * rSquared):
            
        return True 
    
    
    return False



def ColisionBalls(ball1, ball2):
    if (detectColision(ball1,ball2)):
        
        result = elastic_collision_complex(ball1 , ball2)

        ball1.velocity , ball2.velocity = result
    
        





# suma , resta , punto , division 

def sumaVector(vector1, vector2 ):
    result0 = vector1[0] + vector2[0] 
    result1 = vector1[2] + vector2[2]
    tercer = [result0,result1]
    return tercer


def restaVector(vector1, vector2 ):
    result0 = vector1[0] - vector2[0] 
    result1 = vector1[2] - vector2[2]
    tercer = [result0, 0 ,result1]
    return tercer

def restaEscalar (vector1 , escalar):
    result= [vector1[0]-escalar, 0 ,vector1[2]-escalar]

    return result

def sumaEscalar (vector1 , escalar):
    result= [vector1[0]+escalar, 0 ,vector1[2]+escalar]

    return result

def puntoProduct(vector1, vector2):
    result = vector1[0]*vector2[0]+vector1[2]*vector2[2]
    return result 
def multiConjugadoVector (vector1 , vector2):    
    vector2[2]= vector2[2]* -1 
    result = [ vector1[0] * vector2[0] + (vector1[2] * vector2[2]) * -1  , vector1[0]*vector2[2]+vector1[2]*vector2[0]]
    #print(result)
    resultdenom = vector2[0]*vector2[0]  +  vector2[2]*vector2[2]
    #print(resultdenom)
    resultv1 = [result[0]/resultdenom, 0 , result[1]/resultdenom]
    return resultv1



    #print(divisionVector(a,b))


def elastic_collision_complex(vector1 , vector2 ):
        p12 = restaVector(vector1.pos , vector2.pos )
        d = puntoProduct(multiConjugadoVector( restaVector(vector1.velocity , vector2.velocity) , p12) ,  p12)

        
        return restaEscalar(vector1.velocity , d ),sumaEscalar(vector2.velocity , d )

def callback_func(caller, timer_event):

    global time
    #print("velocity", sphere.velocity, "last velocity", sphere.last_velocity)
    # print("pos", sphere.pos, "\n")
    sphere_actor.RotateX(sphere.velocity[0]*3*0.37)
    sphere_actor.RotateZ(sphere.velocity[2]*3*0.53)
    
    sphere_actor2.RotateX(sphere.velocity[0]*3*0.37)
    sphere_actor2.RotateZ(sphere.velocity[2]*3*0.53)
    
    SpeedControler(sphere)
    SpeedControler(sphere2)
    
    
    ColisionWall(sphere)
    ColisionWall(sphere2)
    print ("vel sphere : " , sphere.velocity )
    print ("vel sphere2 : " , sphere2.velocity )
    ColisionBalls(sphere, sphere2)
    print ("vel sphere : " , sphere.velocity )
    print ("vel sphere2 : " , sphere2.velocity )
    sphere.actor.SetPosition(sphere.pos[0], sphere.pos[1], sphere.pos[2])
    sphere2.actor.SetPosition(sphere2.pos[0], sphere2.pos[1], sphere2.pos[2])

    time += 0.001
    render_window.Render()

source1 = vtk.vtkSphereSource()
source1.SetThetaResolution(50)
source1.SetRadius(sphere.radius)
source1.Update()

source2 = vtk.vtkCubeSource()
source2.SetXLength(400)
source2.SetYLength(floor.height)
source2.SetZLength(400)
source2.Update()

source3 = vtk.vtkCubeSource()
source3.SetXLength(400)
source3.SetYLength(wallup.height)
source3.SetZLength(1)
source3.Update()

source4 = vtk.vtkCubeSource()
source4.SetXLength(400)
source4.SetYLength(walldown.height)
source4.SetZLength(1)
source4.Update()

source5 = vtk.vtkCubeSource()
source5.SetXLength(1)
source5.SetYLength(wallleft.height)
source5.SetZLength(400)
source5.Update()

source6 = vtk.vtkCubeSource()
source6.SetXLength(1)
source6.SetYLength(wallright.height)
source6.SetZLength(400)
source6.Update()

#mapper
#sphere_mapper = vtk.vtkPolyDataMapper()
#sphere_mapper.SetInputData(source1.GetOutput())
floor_mapper = vtk.vtkPolyDataMapper()
floor_mapper.SetInputData(source2.GetOutput())
#wallup_mapper = vtk.vtkPolyDataMapper()
#wallup_mapper.SetInputData(source3.GetOutput())
#walldown_mapper = vtk.vtkPolyDataMapper()
#walldown_mapper.SetInputData(source4.GetOutput())
#wallleft_mapper = vtk.vtkPolyDataMapper()
#wallleft_mapper.SetInputData(source5.GetOutput())
#wallright_mapper = vtk.vtkPolyDataMapper()
#wallright_mapper.SetInputData(source6.GetOutput())

## sphere 
map_to_sphere = vtk.vtkTextureMapToSphere()
map_to_sphere.SetInputConnection(source1.GetOutputPort())




# Create mapper and set the mapped texture as input
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(map_to_sphere.GetOutputPort())




map_to_sphere_dos = vtk.vtkTextureMapToSphere()
map_to_sphere_dos.SetInputConnection(source1.GetOutputPort())


# Create mapper and set the mapped texture as input
mapperdos = vtk.vtkPolyDataMapper()
mapperdos.SetInputConnection(map_to_sphere_dos.GetOutputPort())


#texturedos


'''
## Floor

map_to_Floor = vtk.vtkTextureMapToPlane()
map_to_Floor.SetInputConnection(source2.GetOutputPort())
#map_to_Floor.PreventSeamOn()

# Create mapper and set the mapped texture as input
mapperFloor = vtk.vtkPolyDataMapper()
mapperFloor.SetInputConnection(map_to_Floor.GetOutputPort())
'''
## Walls

## 1

wallup_mapper = vtk.vtkTextureMapToPlane()
wallup_mapper.SetInputConnection(source3.GetOutputPort())
# Create mapper and set the mapped texture as input
mapperWall1 = vtk.vtkPolyDataMapper()
mapperWall1.SetInputConnection(wallup_mapper.GetOutputPort())


## 2

wallup_mapper2 = vtk.vtkTextureMapToPlane()
wallup_mapper2.SetInputConnection(source4.GetOutputPort())
# Create mapper and set the mapped texture as input
mapperWall2 = vtk.vtkPolyDataMapper()
mapperWall2.SetInputConnection(wallup_mapper2.GetOutputPort())


## 3

wallup_mapper3 = vtk.vtkTextureMapToPlane()
wallup_mapper3.SetInputConnection(source5.GetOutputPort())
# Create mapper and set the mapped texture as input
mapperWall3 = vtk.vtkPolyDataMapper()
mapperWall3.SetInputConnection(wallup_mapper3.GetOutputPort())


## 4

wallup_mapper4 = vtk.vtkTextureMapToPlane()
wallup_mapper4.SetInputConnection(source6.GetOutputPort())
# Create mapper and set the mapped texture as input
mapperWall4 = vtk.vtkPolyDataMapper()
mapperWall4.SetInputConnection(wallup_mapper4.GetOutputPort())







#actor
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(mapper)
#sphere_actor.GetProperty().SetColor(0, 1, 0.0)
#sphere_actor.GetProperty().SetOpacity(0.5)
sphere.actor = sphere_actor
sphere_actor.SetTexture(texture)



sphere_actor2 = vtk.vtkActor()
sphere_actor2.SetMapper(mapperdos)
#sphere_actor2.GetProperty().SetColor(0, 1, 0.0)
#sphere_actor.GetProperty().SetOpacity(0.5)
sphere2.actor= sphere_actor2
sphere_actor2.SetTexture(texturedos)

floor_actor = vtk.vtkActor()
floor_actor.SetMapper(floor_mapper)
floor_actor.GetProperty().SetColor(60 / 255, 85 / 255, 70 / 255)
#sphere_actor.GetProperty().SetOpacity(0.7)
floor.actor = floor_actor


wallup_actor = vtk.vtkActor()
wallup_actor.SetMapper(mapperWall1)
#wallup_actor.GetProperty().SetColor(1, 1, 1)
wallup.actor = wallup_actor
wallup_actor.SetTexture(textureWall)

walldown_actor = vtk.vtkActor()
walldown_actor.SetMapper(mapperWall2)
#walldown_actor.GetProperty().SetColor(1, 1, 1)
walldown.actor = walldown_actor
walldown_actor.SetTexture(textureWall)

wallleft_actor = vtk.vtkActor()
wallleft_actor.SetMapper(mapperWall3)
#wallleft_actor.GetProperty().SetColor(1, 1, 1)
wallleft.actor = wallleft_actor
wallleft_actor.SetTexture(textureWall)

wallright_actor = vtk.vtkActor()
wallright_actor.SetMapper(mapperWall4)
#wallright_actor.GetProperty().SetColor(1, 1, 1)
wallright.actor = wallright_actor
wallright_actor.SetTexture(textureWall)

#camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,-80,0)
camera.SetPosition(0,sphere.pos[1] * 130 , sphere.pos[1]*150)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(sphere_actor)
renderer.AddActor(floor_actor)
renderer.AddActor(wallup_actor)
renderer.AddActor(walldown_actor)
renderer.AddActor(wallleft_actor)
renderer.AddActor(wallright_actor)
renderer.AddActor(sphere_actor2)
renderer.SetActiveCamera(camera)

#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(1200, 1200)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()

set_initial_position()

interactor.CreateRepeatingTimer(1)
interactor.AddObserver("TimerEvent", callback_func)
interactor.Start()
