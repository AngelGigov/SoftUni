rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(el) for el in input().split()])

#print(matrix)

total = 0

for row_index in range(rows):
    total += matrix[row_index][row_index]

print(total)

