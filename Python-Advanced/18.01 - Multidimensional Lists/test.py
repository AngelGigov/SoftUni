# matrix = []
#
# for i in range(3):
#     matrix.append([])
#     for j in range(1, 4):
#         matrix[i].append(0)
#
# print(matrix)
#
# a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
#
# for row in a:
#     print(len(row))



# matrix = [[1, 2, 3], [4, 5, 6]]
# # flattened = [num for sublist in matrix for num in sublist]
# # print(flattened)

# flattened = []
# for sublist in matrix:
#     for el in sublist:
#         flattened.append(el)
# print(flattened)

#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in range(len(matrix)):
#     for col in range(len(matrix[row])):
#         print(matrix[row][col])


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row_index in range(len(matrix)):
#     for col_index in range(len(matrix[row_index])):
#         print(matrix[row_index][col_index])
#
# a = "ABC"
# list_to_test = [str(i) for i in a]
# print(list_to_test)
# matrix = [input().split() for i in range(5)]
#
# print(matrix)

def valid_coordinates(row, col):
    if {row}.issubset(r) and {col}.issubset(r):
        return True
    else:
        return False

r = range(3)

print(valid_coordinates(1, 3))