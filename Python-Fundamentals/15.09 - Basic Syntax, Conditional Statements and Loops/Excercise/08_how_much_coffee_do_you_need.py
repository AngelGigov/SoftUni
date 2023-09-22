#User input
command = input()
coffee_needed = 0

#Logic
while command != "END":
    if command.islower():
        if command.lower() == 'coding':
            coffee_needed += 1
        elif command.lower() == 'cat' or command.lower() == 'dog':
            coffee_needed += 1
        elif command.lower() == 'movie':
            coffee_needed += 1
        else:
            command = input()
            continue

    elif command.isupper():
        if command.lower() == 'coding':
            coffee_needed += 2
        elif command.lower() == 'cat' or command.lower() == 'dog':
            coffee_needed += 2
        elif command.lower() == 'movie':
            coffee_needed += 2
        else:
            command = input()
            continue
    command = input()

#Print output
if coffee_needed > 5:
    print('You need extra sleep')
else:
    print(coffee_needed)
