thisset = {"apple", "banana", "cherry"}
print(thisset)
print(type(thisset))


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)# duplicate value got ignored




thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  #True and 1 is considered the same value

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)   #False and 0 is considered the same value



thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  #{'apple', 'banana', 'orange', 'cherry'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset) #{'banana', 'mango', 'cherry', 'apple', 'papaya', 'pineapple'}