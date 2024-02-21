#Split list in half and store ele two diffrent list

number = [10,20,30,40]
split1 = []
split2 = []
for i in range(len(number)):
    if i % 2 == 0:
      split1.append(number[i])
    else:
      split2.append(number[i])
print("Split list into two parts:\nPart 1: ", split1,"\nPart 2: ",split2)
