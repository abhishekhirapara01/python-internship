#Interchange first and last ele in list

Mylist = [50,20,30,40,10]
print("\nOriginal List : ", Mylist)
# Swapping the elements using a temporary variable
temp = Mylist[0] 
Mylist[0] = Mylist[-1]
Mylist[-1] = temp
print(f"List after swapping the first and last element: {Mylist}\n")