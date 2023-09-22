# User input
low_limit = int(input())
up_limit = int(input())
magic_number = int(input())

# Logic
counter = 0
is_found = False
for i in range(low_limit, up_limit +1 ):
    if is_found:
        break
    for j in range(low_limit, up_limit + 1):
        if is_found:
            break
        counter += 1
        if i + j == magic_number:
            print(f'Combination N:{counter} ({i} + {j} = {magic_number})')
            is_found = True



# Print output

if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")
