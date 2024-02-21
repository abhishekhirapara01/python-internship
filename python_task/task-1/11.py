#Create a flat list out a of a given list using built-in function
#-------
# Mylist = [15,2224,3,[6789],"Hello",[10,20,30],[4,5]]
# print(Mylist)

def flatten_sum(Lists):
  print(sum(Lists, []))
Lists = [
[9, 3, 8, 3],
[4, 5, 2, 8],
[6, 4, 3, 1],
[1, 0, 4, 5],
]
flatten_sum(Lists)