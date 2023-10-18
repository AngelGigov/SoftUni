targets = [int(x) for x in input().split()]

command = input()

while command != 'End':

    index_target = int(command)

    if index_target < len(targets):
        value_of_the_target = targets[index_target]
    else:
        command = input()
        continue

    targets[index_target] = -1

    for el, value in enumerate(targets):
        if value > value_of_the_target and value != -1:
            targets[el] -= value_of_the_target
        elif value <= value_of_the_target and value != -1:
            targets[el] += value_of_the_target


    command = input()

shoot_targets = targets.count(-1)
list_to_str = [str(x) for x in targets]

print(f"Shot targets: {shoot_targets} -> {' '.join(list_to_str)}")