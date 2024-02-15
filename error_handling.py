# try:
#   age = int(input("Enter your age: "))
# except ValueError:
#   print("Invalid input. Please enter a valid input.")


#raise keywords
def divide(a, b):
  if b == 0:
    raise ValueError("Cannot divide by zero.")   
  #ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.
  return a / b

try:
  result = divide(10, 0)
  print(result)
except ValueError:
  print("An error occurred.")


x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")



#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("abhi.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  