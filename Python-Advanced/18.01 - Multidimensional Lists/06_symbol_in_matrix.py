rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append(list(input()))

special_symbol = input()

is_found = False

for row_index in range(len(matrix)):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == special_symbol:
            is_found = True
            break
    if is_found:
        break

if is_found == True:
    print(f"({row_index}, {col_index})")
else:
    print(f'{special_symbol} does not occur in the matrix')