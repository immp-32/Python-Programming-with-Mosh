
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[1][2] = 50
print(matrix[2][1])

print(matrix)

# Using nested loop for iterating the items
for row in matrix:
    for item in row:
        print(item)