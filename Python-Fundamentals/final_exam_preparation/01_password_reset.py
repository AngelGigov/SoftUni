password = input()
new_password = password

command = input().split()
while command[0] != "Done":
    if command[0] == "TakeOdd": #We iterate thru the string and get only odd numbers
        current_password = new_password
        new_password = ''
        for index, letter in enumerate(current_password):
            if index % 2 != 0:
                new_password = new_password + letter
        print(new_password)

    elif command[0] == "Cut":
        index, lenght = int(command[1]), int(command[2])
        new_password = new_password[:index] + new_password[(index + lenght):]
        print(new_password)
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print('Nothing to replace!')

    command = input().split()

print(f'Your password is: {new_password}')