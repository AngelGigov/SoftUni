# Solution 1
matrix = []

for row in range(int(input())):
    matrix.append([int(el) for el in input().split(', ') if int(el) % 2 == 0])

print(matrix)

# Solution 2 with comprehensions

# matrix = [[ int(column) for column in input().split(', ') if int(column) % 2 == 0 ]for row in range(int(input()))]
# print(matrix)