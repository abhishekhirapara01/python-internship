#inheritance

class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

d = Dog()
d.speak()
#d.bark()



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Abhishek", "Hirapara", 2024)
x.welcome()
