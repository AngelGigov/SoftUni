row, column = [int(el) for el in input().split(', ')]

total = 0
matrix = []

for i in range(row):
    matrix.append([int(el) for el in input().split(', ')])
    total += sum(matrix[i])

print(total)
print(matrix)