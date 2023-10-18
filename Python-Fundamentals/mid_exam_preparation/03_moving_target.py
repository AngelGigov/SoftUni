targets = [int(x) for x in input().split()]

command = input().split()

while command[0] != 'End':

    action, index, value = command[0], int(command[1]), int(command[2])

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= int(value)
            if targets[index] <= 0:
                targets.pop(index)
        else:
            command = input().split()
            continue
    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
            command = input().split()
            continue
    elif action == "Strike":
        start = index - value
        stop = index + value

        if start >= 0 and stop < len(targets):
            del targets[start : stop + 1]
        else:
            print("Strike missed!")
            command = input().split()
            continue

    command = input().split()

list = [str(x) for x in targets]

print('|'.join(list))


