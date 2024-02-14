thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(type(thistuple))



thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  #('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])  #('apple', 'banana', 'cherry', 'orange')




thistuple = ("apple", "banana", "cherry")
y = list(thistuple)     #coverted into list
y.append("orange")
thistuple = tuple(y)  


