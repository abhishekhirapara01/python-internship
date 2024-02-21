#Square each ele of the list and print list in reverse order

number = [1,2,3,4,5]
square_list=[] 

for i in number:
  square_list.append(i**2)
print("Original List : ",number)
print("List after squaring : ",square_list)

#Reverse Order
reverse_order = square_list[::-1]
print("List in reverse order : ",reverse_order)