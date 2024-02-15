age = 21
intro = "My name is abhishek, my age is {}"
print(intro.format(age))



#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "Abhi", age = 16)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("Abhi",16)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("Abhi",16)

print(txt1)
print(txt2)
print(txt3)
