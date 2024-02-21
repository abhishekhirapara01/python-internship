#Find largest and smallest ele in the list

num = int(input(f"Enter the number of elements in list: "))
listofnum = []
for i in range(num):
  ele = input(f"Enter element {i+1}: ")
  listofnum.append(int(ele))

print("\nList is :", listofnum)

smallest_number = listofnum[0]
largest_number =  listofnum[0]
for  j in listofnum:
  if  smallest_number > j:
    smallest_number = j
  elif largest_number < j:
       largest_number=j
print("\nSmalest number: ", smallest_number)
print("Largest number: ", largest_number)
    