#Count and filter odd and even numbers of given list using loops

number = [1,2,3,4,5,6,7,8,9,10]
list1 = []
list2 = []
odd_count = 0
even_count = 0

for i in number:
    if i % 2 == 0:
        list1.append(i)
        even_count += 1
    else:
        list2.append(i)
        odd_count += 1
print("List1: ",list1,"\nEven Count: ",even_count)
print("List2: ",list2,"\nOdd Count: ",odd_count)