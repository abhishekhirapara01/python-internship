a = 33
b = 200
if b > a:
  print("b is greater than a")



a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")



a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")   #without elif


if a > b: print("a is greater than b")



a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")




i = 1
while i < 6:
  print(i)
  i += 1


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


for x in range(6):
  print(x)