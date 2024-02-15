import re

#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("The", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")



#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)


#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)


