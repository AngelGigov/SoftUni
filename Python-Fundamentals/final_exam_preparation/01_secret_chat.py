message = input()

command = input().split(':|:')
while command[0] != "Reveal":
    if command[0] == 'InsertSpace':
        index = int(command[1])
        message = message[:index] + " " + message[index:]
    elif command[0] == "Reverse":
        if command[1] in message:
            reversed_substring = command[1][::-1]
            message = message.replace(command[1], '')
            message = message + reversed_substring
        else:
            print('error')
            command = input().split(':|:')
            continue
    elif command[0] == "ChangeAll":
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)

    print(message)
    command = input().split(':|:')

print(f'You have a new text message: {message}')