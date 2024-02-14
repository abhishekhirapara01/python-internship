a = "Hello, World!"
print(a[1])
print(len(a))

#LOOP FOR STR
for x in "banana":
  print(x)

#CHECK
  txt = "The best things in life are free!"
print("free" in txt)

text = "The best things in life are free!"
if "free" in text:
  print("Yes, 'free' is present.")

#SLICING STRING
  b = "Hello, World!"
print(b[2:5]) #(5 not included)

b = "Hello, World!"
print(b[:5]) #from the start

b = "Hello, World!"
print(b[1:]) #from the end


#MODIFYING STRING

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())


#removes any whitespace from the beginning or the end
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))


#split() method splits the string into substrings if it finds instances of the separator
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#formating string
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
