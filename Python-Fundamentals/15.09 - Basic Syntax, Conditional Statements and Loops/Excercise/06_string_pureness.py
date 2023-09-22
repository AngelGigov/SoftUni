#User Input
number = int(input())

#Logic
for i in range(number):
    get_text = input()
    is_pure = True
    for i in range(len(get_text)):
        letter = get_text[i]
        if letter == ',' or letter == '.' or letter == '_':
            is_pure = False
            break

    if is_pure:
        print(f'{get_text} is pure.')
    else:
        print(f'{get_text} is not pure!')
