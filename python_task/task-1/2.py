#Split list in half and store ele two diffrent list

# number = [10,20,30,40]
# split1 = []
# split2 = []
# for i in range(len(number)):
#     if i % 2 == 0:
#       split1.append(number[i])
#     else:
#       split2.append(number[i])
# print("Split list into two parts:\nPart 1: ", split1,"\nPart 2: ",split2)


lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lst1=[]
lst2=[]
for i in range(0, len(lst)//2):
  lst1.append(lst[i])
for j in range(len(lst)//2, len(lst)):
  lst2.append(lst[j])

print("List part 1: ",lst1)
print("List part 2: ",lst2)
 