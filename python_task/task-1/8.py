#Remove all occurrences of an elements from a given list  

lst=[2,1,3,4,5,7,8,9,8,6,2,2,6]
for i in lst:
  cnt=lst.count(i)
  if cnt>1:
   while i in lst:
      lst.remove(i)
print(lst)
