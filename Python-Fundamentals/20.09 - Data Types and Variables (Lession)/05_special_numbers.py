#Read Input
integer = int(input())

#Logic

for i in range(1, integer + 1):
    number = 0
    integer_to_str = str(i)
    for j in integer_to_str:
        number += int(integer_to_str)

    #print(f'{i} -> {False}')


