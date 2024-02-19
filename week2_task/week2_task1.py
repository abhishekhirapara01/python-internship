class Vehicles:
  def __init__(self,make,model,year,fuel):
    self.BrandName = make
    self.ModelName = model
    self.year = year
    self.fuel = fuel

  def vehicle_information(self):
    print("This is Base class 'Vehicles': ")
    print("BrandName: ",self.BrandName)
    print("ModelName: ",self.ModelName)
    print("Made in year: ",self.year)
    print("Capacity of liters: ",self.fuel)

class Car(Vehicles):
  def __init__(self, make, model, year, fuel,num_doors,trunk_capacity):
    super().__init__(make, model, year, fuel)
    self.Numbers_Doors = num_doors
    self.Trunk_Capacity = trunk_capacity

  def car_information(self):
    print("\nThis is Derived class 'Car': ")
    print("BrandName: ",self.BrandName)
    print("ModelName: ",self.ModelName)
    print("Made in year: ",self.year)
    print("Capacity of liters: ",self.fuel)
    print("Number of doors: ",self.Numbers_Doors)
    print("Capacity of car trunk: ",self.Trunk_Capacity)

class Motorcycle(Vehicles):
  def __init__(self, make, model, year, fuel,has_sidecar,top_speed):
    super().__init__(make, model, year, fuel)
    self.SideCar = has_sidecar
    self.TopSpeed = top_speed

  def Motorcycle_information(self):
    print("\nThis is Derived class 'Motorcycle': ")
    print("BrandName: ",self.BrandName)
    print("ModelName: ",self.ModelName)
    print("Made in year: ",self.year)
    print("Capacity of liters: ",self.fuel)
    print("Has a side-car: ",self.SideCar)
    print("MotorCycle top speed is: ",self.TopSpeed)

a = Vehicles("Hyundai","Creta",2022,5)
b = Car("Toyota","Fortuner",2021,6,4,10)
c = Motorcycle("Hero","Splender",2020,4,2,100)
a.vehicle_information()
b.car_information()
c.Motorcycle_information()