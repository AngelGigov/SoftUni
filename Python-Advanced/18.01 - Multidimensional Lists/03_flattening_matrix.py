# Solution 1 Long

# flat_matrix = []
#
# for sublist in range(int(input())):
#     for el in input().split(', '):
#         flat_matrix.append(int(el))
#
# print(flat_matrix)

#Solution 2 Short

flat_matrix = [int(el) for _ in range(int(input())) for el in input().split(', ')]
print(flat_matrix)

a = copy.deepcopy(flat_matrix)