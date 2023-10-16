list = input().split('!')

command = input()
while command != "Go Shopping!":
    split_command = command.split()
    if split_command[0] == "Urgent":
        if split_command[1] not in list:
            list.insert(0, split_command[1])
        else:
            command = input()
            continue
    elif split_command[0] == "Unnecessary":
        if split_command[1] in list:
            list.remove(split_command[1])
        else:
            command = input()
            continue
    elif split_command[0] == 'Correct':
        if split_command[1] in list:
            item_index = list.index(split_command[1])
            list[item_index] = split_command[2]
        else:
            command = input()
            continue
    elif split_command[0] == 'Rearrange':
        if split_command[1] in list:
            list.remove(split_command[1])
            list.append(split_command[1])
        else:
            command = input()
            continue
    command = input()

print(', '.join(list))