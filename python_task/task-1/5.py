#Print elements With Frequency greater than a given value K
#----

Mylist = [2,4,4,4,3,3,3,8,8,8,2]
K = 2
Mylist2 = []

for i in Mylist:
  freq = Mylist.count(i)
  if (freq > K and i not in Mylist2) :
    Mylist2.append(i)
print("Elements: ",Mylist2)