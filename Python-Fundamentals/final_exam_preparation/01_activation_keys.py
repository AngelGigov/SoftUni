raw_activation_key = input()

command = input().split(">>>")
while command[0] != "Generate":

    if command[0] == "Contains":
        substring = command[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print('Substring not found!')

    elif command[0] == "Flip":
        method, start_index, end_index = command[1], int(command[2]), int(command[3])
        if method == "Upper":
            portion = raw_activation_key[start_index:end_index]
            raw_activation_key = raw_activation_key[:start_index] + portion.upper() + raw_activation_key[end_index:]
            print(raw_activation_key)
        elif method == "Lower":
            portion = raw_activation_key[start_index:end_index]
            raw_activation_key = raw_activation_key[:start_index] + portion.lower() + raw_activation_key[end_index:]
            print(raw_activation_key)
    elif command[0] == "Slice":
        start_index, end_index = int(command[1]), int(command[2])
        portion = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(portion, '')
        print(raw_activation_key)

    command = input().split(">>>")

print(f'Your activation key is: {raw_activation_key}')