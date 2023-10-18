#User input
loot = [x for x in input().split("|")]
command = input().split()

#Logic
while command[0] != "Yohoho!":

    if command[0] == 'Loot':
        for item in command[1:len(command)]:
            if item not in loot:
                loot.insert(0, item)

    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 < index < len(loot):
            item = loot.pop(index)
            loot.append(item)

    elif command[0] == 'Steal':
        lenght = len(loot)
        removed_items = []
        if int(command[1]) <= lenght:
            for item in range(int(command[1])):
                current_item = loot.pop(-1)
                removed_items.insert(0, current_item)
        else:
            for item in range(len(loot)):
                current_item = loot.pop(-1)
                removed_items.insert(0, current_item)
        print(', '.join(removed_items))


    command = input().split()

#Print Output
if len(loot) > 0:
    count = 0
    for item in loot:
        count += len(item)
    avarage_gain = count / len(loot)
    print(f"Average treasure gain: {avarage_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")


