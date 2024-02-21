#Remove empty list from a given list

def  remove_empty(lst):
  return [i for i in lst if i]
print(remove_empty([1,2,3,[],4,5,"",6]))  