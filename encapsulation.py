#encapsulation

class employee:
  def __init__(self,name,age,salary):
    self.name = name
    self.age = age
    self.__salary = salary #private member 
  def get_salary(self):
    return self.__salary
  def set_salary(self,new_salary):
    self.__salary =  new_salary
  def display(self):
    print("Employee Name: ",self.name)
    print("Employee Age: ",self.age)
    print("Employee Salary: ",self.__salary)
s=employee("Abhishek Hirapara",21,20000)
s.display()



class Base:
  def __init__(self):
    self.a = "\nAbhi Patel"
    self._b = "Lj university" #protected member
    self.__c = "Master Of Computer Application" #private member

class Derived(Base):
  def __init__(self):
    Base.__init__(self)
    #print("Calling protected member of base class: ")
    #print(self._b)
    print("Calling private member of base class: ")
    print(self.__c)
obj1 = Base()
print(obj1.a)
print(obj1._b)
#print(obj1.__c)


class BankAccount:
  def __init__(self,name,balance):
    self.name = name
    self.__balance = balance

  def deposite(self,amount):
    self.__balance += amount
    print("Your amount deposite succesfully, You new balance is: ",self.__balance)

  def withdraw(self,amount):
    if amount > self.__balance:
      print("Insufficient balance.")
    else:
      self.__balance -= amount
      print("Withdraw succesfully, You new balance is: ",self.__balance)
Account=BankAccount("Ravi Khimani",1500)
Account.deposite(500)
Account.withdraw(1000)

    