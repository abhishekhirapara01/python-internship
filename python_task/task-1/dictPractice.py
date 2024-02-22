#given key already exists in a dictionary
D = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key(x):
  if x in D:
    print("key is already exists.\n")
  else:
    print("\nkey is not exists.")

key(7)
key(3)


#Merge two Python dictionaries
DI1={'a':100,'b':200}
DI2={'c':300,'d':400}

DI=DI1.copy()
DI.update(DI2)
print(DI)


#Remove a key from a dictionary
D = {'name':'John','age':30,'city':'New York'}
print('Before Removing')
print(D)

del D['name']
print('\nAfter Removing')
print(D)


#Add a key value pair to a dictionary
D = {'name':'John','age':30,'city':'New York'}
print('Original Dictionary')
print(D)

D['country']='USA'
print('\nDictionary After Adding Key')
print(D) 


#Accessing values using keys
D = {'name':'John','age':30,'city':'New York'}
print('Value Accessed Using Key : name')
print(D['name'])


#Accessing all values of a dictionary
V = D.values()
print('\nValues Accessed Using values Method')
for v in V:
    print(v)


#Accessing all keys of a dictionary
Ks = D.keys()
print('\nKeys Accessed Using keys Method')
for k in Ks:
    print(k)
    
N = len(D)
print('\nNumber of Keys in the Dictionary : %d'%N)  


