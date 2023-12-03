password = input()

command = input().split()

while command[0] != "Complete":

    if command[0] == "Make":

        if command[1] == 'Upper':
            index = int(command[2])
            letter_at_index = password[index]
            password = password[:index] + letter_at_index.upper() + password[index + 1:]
            print(password)
        elif command[1] == 'Lower':
            index = int(command[2])
            letter_at_index = password[index]
            password = password[:index] + letter_at_index.lower() + password[index + 1:]
            print(password)
    elif command[0] == "Insert":
        index, char = int(command[1]), command[2]
        if index > len(password):
            command = input().split()
            continue
        else:
            password = password[:index] + char + password[index:]
    elif command[0] == "Replace":
        char, value = command[1], int(command[2])
        to_replace = chr(ord(char)+value)
        password = password.replace(char, to_replace)
        print(password)

    elif command[0] == "Validation":
        if len(password) < 8:
            print("Password must be at lest 8 characters long!")
        if not password.isalnum() and "_" in password:
            print("Password must consist only of letters, digits and _!")
        digits = 0
        for i in password:
            if i.isdigit():
                digits += 1
        if digits < 1:
            print('Password must consist at least one digit!')
        upper_case = 0
        for i in password:
            if i.isupper():
                upper_case += 1
        if upper_case < 1:
            print('Password must consist at least one uppercase letter!')
        lower_case = 0
        for i in password:
            if i.islower():
                lower_case += 1
        if lower_case < 1:
            print('Password must consist at least one lowercase letter!')

    command = input().split()