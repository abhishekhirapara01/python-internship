name = ["ravi", "shyam", "krishna", "ravi"]
print(name)
print(len(name))
print(type(name))



list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(type(list1))
print(type(list2))
print(type(list3))


list4 = ["abc", 34, True, 40, "male"]
print(type(list4))


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")




thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  #['apple', 'blackcurrant', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)  #['apple', 'banana', 'watermelon', 'cherry']



thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) #last to add  ['apple', 'banana', 'cherry', 'orange']



thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) #merge two lists  

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  #remove banana


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)  #['banana', 'cherry']




thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


thislist = ["mango","apple", "banana", "cherry"]
i= 0  
while i < len(thislist):
  print(thislist[i])
  i = i+1





fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)   #['apple', 'banana', 'mango']