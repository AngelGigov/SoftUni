rows = int(input())

for i in range(1, rows + 1):
    for j in range(0, i):
        print('*', end='')
    print()
for i in range(rows - 1, 0, - 1):
    for j in range(0, i):
        print('*', end='')
    print()