#  Read User Input
num = int(input())

counter = 0

#  Logic
for n_1 in range(0, num + 1):
    for n_2 in range(0, num + 1):
        for n_3 in range(0, num + 1):
            sum = n_1 + n_2 + n_3
            if sum  == num:
                counter += 1

print(counter)
