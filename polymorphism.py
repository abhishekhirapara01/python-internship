#Polymorphism

class car:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive....\n")

class boat:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail....\n")

class plain:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly....\n")

car1 = car("\nHyundai","City")
boat1 = boat("Ibiza","Touring")
plain1 = plain("Boing",747)

for x in (car1,boat1,plain1):
  print(x.brand)
  print(x.model)
  x.move()



#example 2
class shape:
  def draw(self):
    pass

class Circle:
  def draw(self):
    print("drawing a circle")

class Rectangle:
  def draw(self):
    print("drawing a rectangle")

class Triangle:
  def draw(self):
    print("drawing a triangle")

shapes = [Circle(),Rectangle(),Triangle()]

for shape in shapes:
  shape.draw()