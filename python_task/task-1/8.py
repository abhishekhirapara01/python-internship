#Remove all occurances of an elements from a given list
#-------

def del_list(lst):
  lst = list(lst)
  del lst
  print(lst)
del_list([1,2,3,4,5])