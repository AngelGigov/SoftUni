number = int(input())
plants_information = {}

for num in range(number):
    plant, rare = input().split("<->")
    if plant not in plants_information.keys():
        plants_information[plant] = {"rarity": rare, "rating": []}
    else:
        plants_information[plant] = {"rarity": rare}

command = input().split(": ")
while command[0] != 'Exhibition':
    if command[0] == "Rate":
        plant, rating = command[1].split(' - ')
        if plant in plants_information.keys():
            plants_information[plant]["rating"].append(float(rating))
        else:
            print('error')
    elif command[0] == "Update":
        plant, new_rarity = command[1].split(' - ')
        if plant in plants_information.keys():
            plants_information[plant]["rarity"] = new_rarity
        else:
            print('error')
    elif command[0] == "Reset":
        plant = command[1]
        if plant in plants_information.keys():
            plants_information[plant]["rating"].clear()
        else:
            print('error')

    command = input().split(": ")


print('Plants for the exhibition:')
for k,v in plants_information.items():
    if plants_information[k]['rating']:
        average_rating = sum(plants_information[k]['rating']) / len(plants_information[k]['rating'])
        print(f'- {k}; Rarity: {plants_information[k]["rarity"]}; Rating: {average_rating:.2f}')
    else:
        print(f'- {k}; Rarity: {plants_information[k]["rarity"]}; Rating: 0.00')