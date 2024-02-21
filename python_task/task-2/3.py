#Swap elements in string list

Mylist = ['Neel','Abhi']
print("\nOriginal List : ", Mylist)
# Swapping the elements using a temporary variable
temp = Mylist[0] 
Mylist[0] = Mylist[1]
Mylist[1] = temp
print(f"List after swapping the first and second element: {Mylist}\n")