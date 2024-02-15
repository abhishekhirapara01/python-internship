
y = 300  #global scope

def student():
  x = 20  #local scope   
  def student2():
    print(x,y)
  student2()   #function inside a function
student()


#same naming variables
a = 2
def myfun():
  a = 3
  print(a)
myfun()
print(a)


#global keyword
def myfun2():
  global y
  y = 200
myfun2()
print(y)

B = 100
def myfun3():
  global B
  B = 200
  #print(B)
myfun3()
print(B)