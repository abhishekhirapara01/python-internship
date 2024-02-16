
#Remove Duplicates From a Python List
def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"]) #dictionary cannot have duplicate keys 

print(mylist)


#Reverse a String in Python
def my_function(x):
  return x[::-1] #slicing

mytxt = my_function("My name is abhishek hirapara")

print(mytxt)


#Add Two Numbers in Python
x = input("Type a number: ")
y = input("Type second number: ")

sum = int(x) + int(y)

print("sum: ", sum)



# maximum of two numbers
def maximum(a, b):
     
    if a >= b:
        return a
    else:
        return b
a = 2
b = 4
print(maximum(a, b))


 
#swap elements
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))


#Revers a list 
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))