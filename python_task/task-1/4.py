#Interchange first and last ele in the list

numbers = [5,2,3,4,1]
print("\nList before swapping first and last elements: ",numbers)

temp = numbers[0]  # store the value of the first element in temp
numbers[0] = numbers[-1]  # replace the first element with the last one
numbers[-1] = temp  # replace the last element with the original first one

print(f"List after swapping first and last elements:   {numbers}\n")