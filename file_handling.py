f = open("abhi.txt",'r')
print(f.read())


f = open("abhi.txt", "r")
print(f.read(5))


f= open("abhi.txt",'r')
print(f.readline())
f.close()


f=open("abhi2.txt","a")
f.write("Now the file has more content!")
f.close()

f = open("abhi2.txt","r")
print(f.read())


f=open("abhi3.txt","w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("abhi3.txt","r")
print(f.read())


#f = open("abhi4.txt","x") #create new file
#f = open("abhi2.txt","x")



#delete file 

import os
# os.remove("abhi4.txt")

if os.path.exists("abhi4.txt"):
  os.remove("abhi4.txt")
else:
  print("The file does not exist")
