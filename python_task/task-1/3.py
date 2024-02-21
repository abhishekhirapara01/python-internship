#Remove multiple empty strings in the list

Mylist = ['apple','','banana','','orange','','','grape']
filtered_list = list(filter(None, Mylist))
print(filtered_list)  