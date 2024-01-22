# First Short Solution (comprehension)

# matrix = [[int(j) for j in input().split()]for el in range(int(input().split(', ')[0]))]


#Second Solution
row, col = [int(el) for el in input().split(', ')]

matrix = []

for _ in range(row):
    data = [int(el) for el in input().split()]
    matrix.append(data)

for col_index in range(col):
    col_total = 0
    for row_index in range(row):
        col_total += matrix[row_index][col_index]
    print(col_total)




# for col_index in range(col):
#     for row_index in range(3):
#         print(sum(col))