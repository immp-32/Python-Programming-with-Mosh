'''
for item in 'Mahesh':
    print(item)

list = ["Mahesh","Samrat","Ashok","Rohit"]
for i in list:
    print(i)


# range function
for i in range(10):
    print(i)

# bypass variable using range
for item in range(0,10,2):
    print(item)
'''
# Exercise
'''
Calculate the total cost of all items of a shopping cart
'''
prices = [10, 43, 50, 30]
total_cost = 0
for price in prices:
    total_cost += price
print(f"Total Cost: {total_cost}")