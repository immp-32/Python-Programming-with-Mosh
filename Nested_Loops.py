'''
for x in range(3):
    for y in range(2):
        print(f'{x}, {y}')

# Exercise using loops
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    print(item * "*")
'''

# using nested loops
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)