def few_shot_examples():
    """
    Provides a set of few-shot examples to guide the model in generating CAD designs using FreeCAD Python scripting.
    
    These examples cover:
    - Basic 3D shapes like cubes, spheres, and cylinders.
    - Parametric CAD modeling techniques, including extrusions and boolean operations.
    - Advanced designs like ball bearings, knobs, and pentagonal columns.
    
    The examples demonstrate key FreeCAD concepts:
    - Sketching and extruding 2D profiles.
    - Constructing solids from geometric primitives.
    - Boolean operations like cut and union.
    - Applying transformations such as translation and rotation.
    - Using loops and mathematical functions to generate complex structures.
    
    These examples ensure the model can handle both fundamental and advanced CAD modeling requests.
    """
    few_shot_example = """
### [User message]
Make the CAD design of a pentagon box (open from one face)

### [Answer]
```python
import Part
import math
from FreeCAD import Base

side_length = 30.0  # Length of each side of the pentagon
height = 20.0  # Height of the pentagon box

App.newDocument("PentagonBox")
App.setActiveDocument("PentagonBox")
App.ActiveDocument = App.getDocument("PentagonBox")
Gui.ActiveDocument = Gui.getDocument("PentagonBox")

pentagon_points = []  # List to hold the points of the pentagon
angle = 360 / 5  # Angle between each vertex of the pentagon

# Calculate the points of the pentagon
for i in range(5):
    x = side_length * math.cos(math.radians(i * angle))
    y = side_length * math.sin(math.radians(i * angle))
    pentagon_points.append(Base.Vector(x, y, 0))

# Create the pentagon wire
pentagon_wire = Part.makePolygon(pentagon_points)
pentagon_face = Part.Face(pentagon_wire)
pentagon_solid = pentagon_face.extrude(Base.Vector(0, 0, height))

Part.show(pentagon_solid)
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

### [User message]
Make a CAD design of a ball-bearing

### [Answer]
```python
import Part
import math
from FreeCAD import Base

# Parameters
R1 = 15.0  # Inner ring inner radius
R2 = 25.0  # Inner ring outer radius
R3 = 30.0  # Outer ring inner radius
R4 = 40.0  # Outer ring outer radius
TH = 15.0  # Thickness of bearing
NBall = 10  # Number of balls
RBall = 5.0  # Ball radius
RR = 1  # Fillet radius
CBall = ((R3 - R2) / 2) + R2  # Ball center radius
PBall = TH / 2  # Ball center height

# Create new document
App.newDocument("BallBearing")
App.setActiveDocument("BallBearing")
App.ActiveDocument = App.getDocument("BallBearing")
Gui.ActiveDocument = Gui.getDocument("BallBearing")

# Inner Ring
inner_cylinder = Part.makeCylinder(R2, TH)
inner_hole = Part.makeCylinder(R1, TH)
InnerRing = inner_cylinder.cut(inner_hole).makeFillet(RR, inner_cylinder.Edges)

# Outer Ring
outer_cylinder = Part.makeCylinder(R4, TH)
outer_hole = Part.makeCylinder(R3, TH)
OuterRing = outer_cylinder.cut(outer_hole).makeFillet(RR, outer_cylinder.Edges)

# Balls
balls = []
for i in range(NBall):
    ball = Part.makeSphere(RBall)
    angle = (i * 2 * math.pi) / NBall
    ball.translate(Base.Vector(CBall * math.cos(angle), CBall * math.sin(angle), TH / 2))
    balls.append(ball)

# Show parts
Part.show(InnerRing)
Part.show(OuterRing)
for ball in balls:
    Part.show(ball)

# Finalize
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

### [User message]
Make a sketch of a circle and then extrude it to make a CAD design of a cylinder.

### [Answer]
```python
import Part
import Sketcher

# Start a new document
doc = App.newDocument()
sketch = doc.addObject("Sketcher::SketchObject", "Sketch")

# Create a circle sketch
sketch.addGeometry(Part.Circle(App.Vector(0, 0, 0), App.Vector(0, 0, 1), 5), False)
doc.recompute()

# Convert to wire
wire = sketch.Shape.Wires[0]
face = Part.Face(wire)

# Extrude the face to create a cylinder
cylinder = face.extrude(FreeCAD.Vector(0, 0, 10))
Part.show(cylinder)
```


### [User message]
Make the CAD design of a knob

### [Answer]
On thinking like a designer, the door knob would look like a hollow sphere and also there would be a cut at one place to 
```python
import Part
OuterSphere=Part.makeSphere(4) #make the outer sphere

#make a cylinder and do cut that cylinder from the sphere
Cylinder = Part.makeCylinder(2, 10) 
DoorKnob = OuterSphere.cut(Cylinder)
Part.show(DoorKnob)
```

### [User message]
Make a cad model of a cube of side length 10, with one of its vertex at origin

### [Answer]
```pythonimport Part
import Sketcher

#create a new document
doc = App.newDocument()

#make box with its starting edge at origin
box = Part.makeBox(10, 10, 10)

#show the box
Part.show(box)
```

### [User message]
Make a cad model of a sphere which has a radius of 10 millimeters and it has its center at location (50, 0, 0)

### [Answer]
```python
import Part
import Sketcher

#create a new document
doc = App.newDocument()

#make a plane which has its origin as (50, 0, 0)
placement = App.Placement(App.Vector(50, 0, 0), App.Rotation()) #creates a plane at this location.
Plane = doc.addObject("Part::Plane", "Plane")
Plane.Placement = placement
Plane.Length = 10  # Set the length of the plane as desired

#always make the visibility of the plane generated as False
Plane.ViewObject.Visibility = False

#Sketch on the plane generated and make sphere with its center at the origin of the plane generated previously
plane_placement = Plane.Placement
plane_location = plane_placement.Base
box_at_plane = Part.makeSphere(10, plane_location)
Part.show(box_at_plane)
```

### [User message]
Make a sketch of a circle and then extrude it to make a CAD design of a cylinder. 

### [Answer]
```python
import Part
import Sketcher

#start a new document
doc = App.newDocument()
sketch = doc.addObject("Sketcher::SketchObject", "Sketch")

#make sketch of a circle.
sketch.addGeometry(Part.Circle(App.Vector(0.2, 0, 0), App.Vector(0, 0, 1), 1), False)
doc.recompute()

#convert it into the format of a wire
wire = FreeCAD.ActiveDocument.Sketch.Shape.Wires[0]
face = Part.Face(wire)

#extrude the face (wire)
extr = face.extrude(FreeCAD.Vector(0,0,10))
Part.show(extr)
```
    """
    return few_shot_example



def get_code_prompt(user_query, steps, example_description):
    
    few_shot_example = few_shot_examples()
    prompt = f"""
### FreeCAD Python API Instructions for CAD Modeling ###

You are a Computer-Aided Design Engineer with extensive industrial experience, proficient in using FreeCAD.
Your task is to generate Python code to create CAD models based on user input.

#### General Guidelines:
1. **Use Modular Functions** - Encapsulate model creation into reusable functions.
2. **Apply Boolean Operations** - Utilize union, subtraction, and intersection for complex models.
3. **Include Parametric Design** - Allow dynamic changes by defining parameters.
4. **Use Constraints** - Ensure accurate dimensions by using geometric constraints.
5. **Implement Lofting and Sweeping** - Generate smooth transitions between sections.
6. **Support Surface and Solid Modeling** - Combine planar and curved surfaces for intricate designs.
7. **Enable Assembly Operations** - Position and align multiple components in a scene.

#### Primary FreeCAD Functions:

##### 1. **Basic Shape Creation**
- `makeBox(length, width, height, [pnt, dir])` → Creates a box.
- `makeCylinder(radius, height, [pnt, dir, angle])` → Creates a cylinder.
- `makeSphere(radius, [center_pnt, axis_dir, V_startAngle, V_endAngle, U_angle])` → Creates a sphere.
- `makeCone(radius1, radius2, height, [pnt, dir, angle])` → Creates a cone.
- `makeTorus(radius1, radius2, [pnt, dir, angle1, angle2, angle])` → Creates a torus.

##### 2. **Advanced Shape Operations**
- `makeLoft(shapelist, [solid, ruled])` → Creates a lofted shape between profiles.
- `makeRevolution(Curve, [vmin, vmax, angle, pnt, dir])` → Revolves a shape around an axis.
- `makeHelix(pitch, height, radius, [angle, lefthand, heightstyle])` → Generates a helical shape.
- `makeTube(edge, float)` → Creates a tube along a given path.
- `makeShell(list)` → Converts a collection of faces into a shell.
- `makeSolid(Part.Shape)` → Converts a shape into a solid.

##### 3. **Boolean Operations**
- `cut(shape1, shape2)` → Subtracts shape2 from shape1.
- `fuse(shape1, shape2)` → Merges shape1 and shape2.
- `common(shape1, shape2)` → Intersects shape1 and shape2.

##### 4. **Transformation & Positioning**
- `translate(shape, Vector(x, y, z))` → Moves an object.
- `rotate(shape, Vector(x, y, z), angle)` → Rotates an object.
- `mirror(shape, plane)` → Mirrors an object across a plane.
- `scale(shape, factor)` → Resizes an object.
- `align(shape1, shape2, method)` → Aligns two objects.

##### 5. **Constraints & Parametric Design**
- Define geometric constraints (`Constraint("Distance", vertex1, vertex2, value)`)
- Define parametric variables (`Length = App.ActiveDocument.addObject("App::FeaturePython", "Length")`)

##### 6. **Assembly & Component Handling**
- `addComponent(assembly, component, position)` → Adds a component to an assembly.
- `setConstraint(assembly, component1, component2, constraintType, value)` → Adds constraints between parts.
    """
    prompt = f"""
### Instructions ###
You are a Computer Aided Design Engineer with a lot of industrial experience. You are proficient in using the FreeCAD software.
Your task is to write the corresponding python code for generating what the user asked, using the FreeCAD library to generate the CAD model. Make sure to follow the steps given. Do not save the code at the end. 
Use the following functions to make simple solids:
1. makeBox(length,width,height,[pnt,dir]) #Description: Makes a box located at pnt with the dimensions (length,width,height). By default pnt is Vector(0,0,0) and dir is Vector(0,0,1)
2. makeCircle(radius,[pnt,dir,angle1,angle2]) #Description: Makes a circle with a given radius. By default pnt is Vector(0,0,0), dir is Vector(0,0,1), angle1 is 0 and angle2 is 360.
3. makeCone(radius1,radius2,height,[pnt,dir,angle]) #Description: Makes a cone with given radii and height. By default pnt is Vector(0,0,0), dir is Vector(0,0,1) and angle is 360
4. makeCylinder(radius,height,[pnt,dir,angle]) #Description: Makes a cylinder with a given radius and height. By default pnt is Vector(0,0,0),dir is Vector(0,0,1) and angle is 360
5. makeHelix(pitch,height,radius,[angle,lefthand,heightstyle]) #Description: Makes a helix shape with a given pitch, height and radius. Defaults to right-handed cylindrical helix. Non-zero angle parameter produces a conical helix. Lefthand True produces left handed helix. Heightstyle applies only to conical helices. Heightstyle False (default) will cause the height parameter to be interpreted as the length of the side of the underlying frustum. Heightstyle True will cause the height parameter to be interpreted as the vertical height of the helix. Pitch is "metric pitch" (advance/revolution). For conical helix, radius is the minor radius.
6. makeLine((x1,y1,z1),(x2,y2,z2)) #Description: Makes a line of two points
7. makeLoft(shapelist<profiles>,[boolean<solid>,boolean<ruled>]) #Description: Creates a loft shape using the list of profiles. Optionally make result a solid (vs surface/shell) or make result a ruled surface.
8. makePlane(length,width,[pnt,dir]) #Description: Makes a plane. By default pnt is Vector(0,0,0) and dir is Vector(0,0,1)
9. makePolygon(list) #Description: Makes a polygon of a list of Vectors
10. makeRevolution(Curve,[vmin,vmax,angle,pnt,dir]) #Description: Makes a revolved shape by rotating the curve or a portion of it around an axis given by (pnt,dir). By default vmin/vmax are set to bounds of the curve,angle is 360,pnt is Vector(0,0,0) and dir is Vector(0,0,1)
11. makeShell(list) #Description: Creates a shell out of a list of faces. Note: Resulting shell should be manifold. Non-manifold shells are not well supported.
12. makeSolid(Part.Shape) #Description: Creates a solid out of the shells inside a shape.
13. makeSphere(radius,[center_pnt, axis_dir, V_startAngle, V_endAngle, U_angle]) #Description: Makes a sphere (or partial sphere) with a given radius. By default center_pnt is Vector(0,0,0), axis_dir is Vector(0,0,1), V_startAngle is 0, V_endAngle is 90 and U_angle is 360
14. makeTorus(radius1,radius2,[pnt,dir,angle1,angle2,angle]) #Description: Makes a torus with a given radii and angles. By default pnt is Vector(0,0,0),dir is Vector(0,0,1),angle1 is 0,angle2 is 360 and angle is 360
15. makeTube(edge,float) #Description: Creates a tube.

These are a few example codes you can take reference from:
### Examples ###
{few_shot_example}

### [User message]
Steps to follow while writing the code are given below: 
{steps}
Follow these steps and generate a Python code using the FreeCAD library to make a CAD design of a {user_query}
with an example description of how the object should roughly look like: {example_description}

### [Answer]
```python
"""
    return prompt


def get_steps_prompt(user_query):
    steps_prompt = f"""
### Instructions ###
You are a Computer-Aided Design (CAD) Engineer with extensive industry experience. You are proficient in mechanical engineering concepts and have in-depth knowledge of FreeCAD software for designing CAD models.

### Task ###
The user has asked: "{user_query}". Your task is to provide a step-by-step guide to design the requested object in FreeCAD. Before listing the steps, first visualize how the 3D model would look. Then, systematically outline the design process. Follow the structured format used in the examples below.

### Examples ###

### [User message]
What is the step-by-step approach to make a CAD design of a rectangular prism?

### [Answer]
Step 1: Create a new document in FreeCAD.
Step 2: Use the `Part.makeBox` function to create a cuboid with the desired dimensions.
Step 3: Use `Part.show` to display the generated part.

### [User message]
What is the step-by-step approach to make a CAD design of a knob?

### [Answer]
Step 1: Create a new document in FreeCAD.
Step 2: Use the `Part.makeSphere` function to create a spherical base.
Step 3: Use the `Part.makeCylinder` function to create a cylinder and position it appropriately.
Step 4: Perform a Boolean cut operation to shape the knob as needed.
Step 5: Use `Part.show` to display the generated part.

### [User message]
What is the step-by-step approach to make a CAD design of a chair?

### [Answer]
Step 1: Create a new document in FreeCAD.
Step 2: Sketch the base profile of the chair’s seat using the Sketcher workbench.
Step 3: Extrude the sketch to form a solid seat.
Step 4: Create additional sketches for the backrest and legs.
Step 5: Extrude or pad these sketches to construct the backrest and legs.
Step 6: Use fillets or chamfers if necessary to refine the edges.

### [User message]
What is the step-by-step approach to make a CAD design of a gear?

### [Answer]
Step 1: Create a new document in FreeCAD.
Step 2: Sketch a single tooth profile using the involute curve.
Step 3: Use the circular pattern tool to replicate the tooth profile around the center.
Step 4: Extrude the profile to give the gear its desired thickness.
Step 5: Add a central hole for a shaft if required.

### [User message]
What is the step-by-step approach to make a CAD design of a wrench?

### [Answer]
Step 1: Create a new document in FreeCAD.
Step 2: Sketch the outline of the wrench, including the handle and jaws.
Step 3: Extrude the sketches to create solid bodies.
Step 4: Add details such as grip patterns or chamfers to refine the design.
Step 5: Use filleting to smooth out sharp edges if necessary.

### [User message]
What is the step-by-step approach to make a CAD design of {user_query}?

### [Answer]
    """
    return steps_prompt

def get_error_prompt(generated_code, error):

    error_prompt = f""" You are an intelligent CAD designer who makes CAD designs using FreeCAD library of python. The user will give you the code he executed and the error message he encountered. 
Your task is to find the error in the code and make the required modifications to it. After making the modifications give the entire modified code. You can take reference from the examples given below. 
    
### Examples ###
### [User message]
The code I worked on is:
```python
import Part
cuboid = Part.Box(1,2,3)
Part.show(cuboid)
```
The error I encountered is:
```
16:03:01  Traceback (most recent call last):
File "C:/Subjects/Semester2/NLP/Project/assignment4/pyautogui/xyz.FCMacro", line 2, in <module>
cuboid = Part.Box(1,2,3)
<class 'AttributeError'>: module 'Part' has no attribute 'Box'
```
### [Answer]
```python
import Part
cuboid = Part.makeBox(1,2,3)
Part.show(cuboid)
```

### [User message]
The code I worked on is
```python
import FreeCAD as App
import Part

# Create a new document
doc = App.newDocument("MyRectangle")

# Define dimensions of the rectangle
length = 10  # Length of the rectangle
breadth = 5    # Width of the rectangle

# Create a rectangle sketch
sketch = doc.addObject('Sketcher::SketchObject', 'RectangleSketch')
sketch.addGeometry(Part.Line(App.Vector(0, 0, 0), App.Vector(length, 0, 0)), False)
sketch.addGeometry(Part.Line(App.Vector(length, 0, 0), App.Vector(length, breadth, 0)), False)
sketch.addGeometry(Part.Line(App.Vector(length, breadth, 0), App.Vector(0, breadth, 0)), False)
sketch.addGeometry(Part.Line(App.Vector(0, breadth, 0), App.Vector(0, 0, 0)), False)
Part.show(sketch)

# Close the sketch
sketch.close()

# Create a pad from the sketch
rectangle = doc.addObject("PartDesign::Pad", "Rectangle")
rectangle.Sketch = sketch
rectangle.Length = 10  # Extrusion length

# Display the document
App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```
The error I encountered is
```
Traceback (most recent call last):
  File "/home/abadagab/results/code/query_3_direct_attempt_2.FCMacro", line 13, in <module>
    sketch.addGeometry(Part.Line(App.Vector(0, 0, 0), App.Vector(length, 0, 0)), False)
<class 'TypeError'>: Unsupported geometry type: Part::GeomLine
```

### [Answer]
```python
import Part
import math
from FreeCAD import Base

length = 30.0
breadth = 20.0
height = 20

#Another way of making the sketch of a rectangle is by appending all the points in this manner and making a wire.
App.newDocument("RectangleBox")
App.setActiveDocument("RectangleBox")
App.ActiveDocument = App.getDocument("RectangleBox")
Gui.ActiveDocument = Gui.getDocument("RectangleBox")
rectangle_points = []
rectangle_points.append(Base.Vector(0, 0, 0))
rectangle_points.append(Base.Vector(length, 0, 0))
rectangle_points.append(Base.Vector(length, breadth, 0))
rectangle_points.append(Base.Vector(0, breadth, 0))
rectangle_points.append(Base.Vector(0, 0, 0))

# Create the rectangle wire
rectangle_wire = Part.makePolygon(rectangle_points)
rectangle_face = Part.Face(rectangle_wire)
rectangle_solid = rectangle_face.extrude(Base.Vector(0, 0, height))
Part.show(rectangle_solid)
App.activeDocument().recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

### [User message]
The code I worked on is
```python
```
The error I encountered is
```
Traceback (most recent call last):
  File "/home/abadagab/results/code/query_0_direct_attempt_1.FCMacro", line 25, in <module>
    rectangle_solid = Part.extrude(rectangle_face, Base.Vector(0, 0, height))
<class 'AttributeError'>: module 'Part' has no attribute 'extrude'
```

### [Answer]
```python
import Part
import math
from FreeCAD import Base

length = 30.0
breadth = 20.0
height = 20

#Another way of making the sketch of a rectangle is by appending all the points in this manner and making a wire.
App.newDocument("RectangleBox")
App.setActiveDocument("RectangleBox")
App.ActiveDocument = App.getDocument("RectangleBox")
Gui.ActiveDocument = Gui.getDocument("RectangleBox")
rectangle_points = []
rectangle_points.append(Base.Vector(0, 0, 0))
rectangle_points.append(Base.Vector(length, 0, 0))
rectangle_points.append(Base.Vector(length, breadth, 0))
rectangle_points.append(Base.Vector(0, breadth, 0))
rectangle_points.append(Base.Vector(0, 0, 0))

# Create the rectangle wire
rectangle_wire = Part.makePolygon(rectangle_points)
rectangle_face = Part.Face(rectangle_wire)
rectangle_solid = rectangle_face.extrude(Base.Vector(0, 0, height)) #This is how the sketch should be extruded

### [User message]
The code I worked on is:
```python
import FreeCAD as App
import Part

doc = App.newDocument("MySphere")

sphere = Part.makeSphere(5)
doc.addObject("Part::Feature", "Sphere").Shape = sphere
App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

The error I encountered is: 
``` Traceback (most recent call last):
  File "/home/user/scripts/macro.FCMacro", line 5, in <module>
    sphere = Part.makeSphere(5)
<class 'AttributeError'>: module 'Part' has no attribute 'makeSphere'
```


### [Answer]
```
import FreeCAD as App
import Part

doc = App.newDocument("MySphere")

sphere = Part.makeSphere(radius=5)  # Corrected method call
doc.addObject("Part::Feature", "Sphere").Shape = sphere
App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")

### [User message]

The code I worked on is:
```
import FreeCAD as App
import Part

doc = App.newDocument("MyCylinder")

cylinder = Part.makeCylinder(5, 10)
doc.addObject("Part::Feature", "Cylinder").Shape = cylinder
App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

The error I encountered is:
```
Traceback (most recent call last):
  File "/home/user/scripts/macro.FCMacro", line 5, in <module>
    cylinder = Part.makeCylinder(5, 10)
<class 'TypeError'>: makeCylinder() takes no positional arguments
```

### [Answer]
```
import FreeCAD as App
import Part

doc = App.newDocument("MyCylinder")

cylinder = Part.makeCylinder(radius=5, height=10)  # Fixed by using keyword arguments
doc.addObject("Part::Feature", "Cylinder").Shape = cylinder
App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

### [User message]
The code I worked on is:
``` import FreeCAD as App
import Part

doc = App.newDocument("CutExample")

box1 = Part.makeBox(10, 10, 10)
box2 = Part.makeBox(5, 5, 5)
box2.translate(App.Vector(2, 2, 2))

cut_result = box1.cut(box2)

doc.addObject("Part::Feature", "CutResult").Shape = cut_result
App.ActiveDocument.recompute()
Gui.activeDocument().activeView().viewAxometric()
Gui.SendMsgToActiveView("ViewFit")
```

The error I encountered is:
``` Traceback (most recent call last):
  File "/home/user/scripts/macro.FCMacro", line 9, in <module>
    cut_result = box1.cut(box2)
<class 'AttributeError'>: 'NoneType' object has no attribute 'cut'
```

### [Answer]

import FreeCAD as App
import Part

doc = App.newDocument("CutExample")

box1 = Part.makeBox(10, 10, 10)
box2 = Part.makeBox(5, 5, 5)
box2.translate(App.Vector(2, 2, 2))

if box1 and box2:  # Ensure objects are valid before performing boolean operation
    cut_result = box1.cut(box2)
    doc.addObject("Part::Feature", "CutResult").Shape = cut_result
    App.ActiveDocument.recompute()
    Gui.activeDocument().activeView().viewAxometric()
    Gui.SendMsgToActiveView("ViewFit")
else:
    print("Error: One of the objects was not created correctly.")

### [User message]
The code I worked on is:
``` python
{
    generated_code
}
```
The error I encountered is
```
{error}
```

### [Answer]
```python
    """
    return error_prompt