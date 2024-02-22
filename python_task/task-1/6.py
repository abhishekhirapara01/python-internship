#Find all possible combination of a list with three elements
#--------
number = [12,24,36]
lst=[]
for j in number:
    lst.append([j])
for i in range(0,len(number)):
    for k in range(i+1,len(number)):
        lst.append([number[i],number[k]])
lst.append(number)
print(lst)
  