n = int(input())

matrix = [[int(el) for el in input().split()]for i in range(n)]

primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - i - 1] for i in range(n)]

print(abs(sum(primary) - sum(secondary)))
