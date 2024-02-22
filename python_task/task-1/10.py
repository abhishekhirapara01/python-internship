#Remove negetive value from a list with filter() method
#------

Mylist = [-21,1,-2,3,45,-78]

def remove_ele(lst):
  return lst > 0

number = list(filter(remove_ele, Mylist))
print(f"filtered list is: {number}")