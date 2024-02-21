#Interchange first and second ele in list

Mylist = [20,10,30,40,50]
print("\nOriginal List : ", Mylist)
# Swapping the elements using a temporary variable
temp = Mylist[0] 
Mylist[0] = Mylist[1]
Mylist[1] = temp
print(f"List after swapping the first and second element: {Mylist}\n")