def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Hirapara")

my_function("Tushar")
my_function("Abhi")
my_function("Sagar")


#This function expects 2 arguments, and gets 2 arguments
def my_function(fname,lname):
  print(fname + " " + lname)
my_function("Abhishek","Hirapara")




def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)



#LAMBDA

x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))