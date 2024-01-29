n = int(input())
matrix = [[int(j) for j in input().split(", ")]for i in range(n)]

primary = [matrix[r][r] for r in range(n)]
secondary = [matrix[r][n - r - 1] for r in range(n)]

print(f'Primary diagonal: {", ".join(str(el) for el in primary)}. Sum: {sum(primary)}')
print(f'Secondary diagonal: {", ".join(str(el) for el in secondary)}. Sum: {sum(secondary)}')
