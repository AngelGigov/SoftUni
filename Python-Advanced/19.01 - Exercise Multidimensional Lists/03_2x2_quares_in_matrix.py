rows, cols = [int(i) for i in input().split()]

matrix = [[j for j in input().split()]for i in range(rows)]


times_found = 0

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        below_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        if current_element == next_element == below_element == diagonal_element:
            times_found += 1

print(times_found)
