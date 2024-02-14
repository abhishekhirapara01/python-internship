class MyClass:
  x = 5
print(MyClass)


class MyClass1:
  x=10
p1 = MyClass1()
print(p1.x)



class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1 = person("ABHI",22)
print(p1.name)
print(p1.age)



class person1:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = person1("ABHI",22)

print(p1)



class person2:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def my_function(self):
    print("Hello My name is " + self.name)
p1 = person2("ABHI",22)
p1.my_function()





