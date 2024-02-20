#Even odd number
num = int(input("Enter a number: "))
if num % 2 == 0:
    print ("The number is even")
else:
  print ("The number is odd")


#Factorial of a number
# num = int(input('Enter the number to find its factorial : '))
# fact=1
# for i in range(1,num+1):
#     fact = fact *i
# print ('The Factorial of',num,'is',fact)


#Reverse a Number
#slicing
# n = int(input("Enter int: "))
# num = str(n)
# result = int(num[::-1])
# print("The reversed number is", result)

#using while loop
# number = int(input("Enter integer numbers: "))
# revsre_num = 0 
# while(number > 0):
#   remainder = number % 10
#   revsre_num = (revsre_num*10) + remainder
#   number = number // 10
# print("The reverse number is: ",revsre_num)


#leap year
# year = int(input("Enter a year: "))
# if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
#     print(f"{year} is a leap year.")
# else:
#     print("This is not a leap year.")


#Convert Celsius to Fahrenheit
# celsius = float(input("Enter temperature in Celsius:"))
# fahrenheit = (celsius * 9/5) + 32
# print("Temperature in Fahrenheit:", fahrenheit)


#prime number
# num = int(input("Enter number: "))
# flag = 0
# if(num == 1):
#   flag = 1
#   print("Not a prime number")
# for i in range(2,num):
#   if(num % i == 0):
#     print("Not a prime number")
#     flag = 1
#     break
# if (flag ==0):
#   print("This is a prime number")


#Fizzbuzz program
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     if(i % 3 == 0 and i % 5 == 0):
#         print("FizzBuzz")
#     elif(i % 3 == 0):
#         print("Fizz")
#     elif(i % 5 == 0):
#         print("Buzz")
#     else:
#         print(i)

