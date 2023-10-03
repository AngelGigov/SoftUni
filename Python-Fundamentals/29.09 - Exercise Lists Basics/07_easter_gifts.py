#User Input
gifts = input().split()
command = input().split()

#Logic
while command[0] != "No" and command[1] != "Money":
    if command[0] == "OutOfStock":
        for i in gifts:
            if i == command[1]:
                gifts[gifts.index(command[1])] = "None"
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]
    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]
    command = input().split()

#Checking and removing "None" from list
while "None" in gifts:
    gifts.remove("None")

#Print Output
print(*gifts)
