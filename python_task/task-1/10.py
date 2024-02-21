#Remove negetive value from a list with filter() method
#------
Mylist = [1,-2,3,-4,5,-6,7,-8]
def num(lst):
  for i in lst:
    if(lst[i]<=0):
      list(lst)
      lst.remove()
filtered_list = filter(num, Mylist)
print(list(filtered_list))