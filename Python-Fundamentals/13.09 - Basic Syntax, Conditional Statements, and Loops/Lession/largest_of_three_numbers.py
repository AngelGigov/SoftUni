number = int(input())

max_number = number

for i in range(2):
    get_number = int(input())
    if get_number > max_number:
        max_number = get_number

print(max_number)

