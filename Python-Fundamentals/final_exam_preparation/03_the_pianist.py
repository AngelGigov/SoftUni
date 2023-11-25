number_of_pieces = int(input())
collection = {}

for number in range(number_of_pieces):
    piece, composer, key = input().split("|")
    collection[piece] = {"composer": composer, "key": key}

command = input().split("|")
while command[0] != 'Stop':
    if command[0] == "Add":
        if command[1] in collection.keys():
            print(f'{command[1]} is already in the collection!')
        else:
            collection[command[1]] = {"composer": command[2], "key": command[3]}
            print(f'{command[1]} by {command[2]} in {command[3]} added to the collection!')
    elif command[0] == "Remove":
        if command[1] in collection.keys():
            item = collection.pop(command[1])
            print(f'Successfully removed {command[1]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')
    elif command[0] == "ChangeKey":
        if command[1] in collection.keys():
            collection[command[1]]["key"] = command[2]
            print(f'Changed the key of {command[1]} to {command[2]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')

    command = input().split("|")

for key, value in collection.items():
    print(f'{key} -> Composer: {value["composer"]}, Key: {value["key"]}')





