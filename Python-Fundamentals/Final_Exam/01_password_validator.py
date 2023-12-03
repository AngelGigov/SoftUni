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
        pass

    command = input().split()