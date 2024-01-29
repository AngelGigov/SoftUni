rows, columns = [int(el) for el in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for column in range(columns):
        matrix[row].append(chr(row + 97) + chr(row + column + 97) + chr(row + 97))

[print(*a) for a in matrix]