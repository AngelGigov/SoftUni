rows, cols = [int(i) for i in input().split()]

matrix = [[int(j) for j in input().split()]for i in range(rows)]


total_sum = float("-inf")
max_sum_matrix = []

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_element = matrix[row_index][col_index]
        first_row = matrix[row_index][col_index:col_index + 3]
        second_row = matrix[row_index + 1][col_index:col_index + 3]
        third_row = matrix[row_index + 2][col_index:col_index + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > total_sum:
            total_sum = current_sum
            max_sum_matrix = [first_row, second_row, third_row]

print(f'Sum = {total_sum}')
[print(*row) for row in max_sum_matrix]