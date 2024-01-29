def valid_coordinates(row, col):
    if {row}.issubset(r) and {col}.issubset(r):
        return True
    else:
        return False

n = int(input())

# matrix = [[int(j) for j in input().split()]for i in range(n)]

r = range(n)

matrix = []
for row in range(n):
    matrix.append([])
    for num in input().split():
        matrix[row].append(int(num))

command = input()
while command != "END":
    action, row_to_be_changed, col_to_be_changed, value = command.split()

    if not valid_coordinates(int(row_to_be_changed), int(col_to_be_changed)):
        print("Invalid coordinates")
    else:
        if action == "Add":
            matrix[int(row_to_be_changed)][int(col_to_be_changed)] += int(value)

        elif action == "Subtract":
            matrix[int(row_to_be_changed)][int(col_to_be_changed)] -= int(value)

    command = input()

[print(*x) for x in matrix]




