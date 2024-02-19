import math

class Shape:
  def __init__(self):
    pass
  def Calculate_area(self):
    pass

class Circle(Shape):
  def __init__(self,radius):
    super().__init__()
    self.Area = radius

  def Calculate_area(self):
    area = math.pi * self.Area ** 2
    print("Area of circle is: ",area)

class Rectangle(Shape):
  def __init__(self,length,width):
    super().__init__()
    self.length = length
    self.width = width

  def Calculate_area(self):
    area = self.length * self.width
    print("Area of Rectangle is: ",area)

a = Shape()
b = Circle(4)
c = Rectangle(2,5)
a.Calculate_area()
b.Calculate_area()
c.Calculate_area()
