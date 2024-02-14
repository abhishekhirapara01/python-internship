#Abstraction

from abc import abstractclassmethod

class Car:
  def __init__(self,brand,model,year):
    self.brand = brand
    self.model = model
    self.year = year

  @abstractclassmethod
  def printingDetails(self):
    pass

  def accelerate(self):
    print("speed up...")

  def break_applied(self):
    print("Car stop")

class Hatchback(Car):
  def printingDetails(self):
    print("Brand: ",self.brand);
    print("Model: ",self.model);
    print("Year: ",self.year);

  def sundroof(self):
    print("Not having feature")

class Suv(Car):
  def printingDetails(self):
    print("Brand: ",self.brand);
    print("Model: ",self.model);
    print("Year: ",self.year);

  def sundroof(self):
    print("Available")

car1 = Hatchback("Maruti","Alto",2001);
car2 = Suv("Mahindra","Thar",2021);

car1.printingDetails
car1.accelerate
car2.printingDetails
car2.accelerate