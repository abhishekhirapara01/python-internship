def calculate():
  num1 = int(input("Enter first num: "))
  num2 = int(input("Enter second num: "))
  operator = input("Enter operators like +,-,/,* : ")

  if operator == "+":
    result = num1 + num2
  elif operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("division by '0' is not allowed")
      return
    result = num1 / num2
  else:
    print("Invalid operator")
  
  print("Result: ",result)
calculate()
