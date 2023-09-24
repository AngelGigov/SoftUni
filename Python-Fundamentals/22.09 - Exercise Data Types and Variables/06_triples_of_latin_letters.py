#Read user input
number = int(input())

#Logic and Print Output
for char_a in range(0, number):
    for char_b in range(0, number):
        for char_c in range(0, number):
            print(f'{chr(97 + char_a)}{chr(97 + char_b)}{chr(97 + char_c)}')