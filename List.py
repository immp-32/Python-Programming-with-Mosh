'''
names =["Mahesh", "Samrat", "Rohit","Sahin"]
names[3] ="Sachin"
print(names)
'''

# Exercise
'''
find the largest number in the list

number = [10, 30, 32, 65, 43]
print(max(number))
print(min(number))

number.sort()
print(number[-1])


# Next Method-------------------------
number = [10, 30, 32, 65, 43]
max = number[0]
for item in number:
    if item > max:
        max = item
print(max)
'''

# List Methods---------------------------
numbers = [10, 32, 54, 5]
numbers.append(64)
numbers.insert(1, 64)

# numbers.remove(5)
# numbers.pop(0)
'''
if 54 in numbers:
    print("Yes it is present in the list")
else:
    print("Oops we cannot find the number")
print(numbers.count(64))
print(numbers)

numbers.sort()
numbers.reverse()
print(numbers)

numbers2 = numbers.copy()
numbers.append(70)
print(numbers)
print(numbers2)
'''

# remove duplicates from the list
marks = [23, 43, 53, 23, 4, 53]
unique = []

for item in marks:
    if item not in unique:
        unique.append(item)
print(unique)