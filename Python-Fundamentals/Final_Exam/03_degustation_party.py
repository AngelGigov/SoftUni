
guest_information = {}
unliked_meals = 0

command = input().split('-')

while command[0] != "Stop":
    guest = command[1]
    meal = command[2]
    if command[0] == "Like":
        if guest not in guest_information.keys():
            guest_information[guest] = []
        if meal not in guest_information[guest]:
            guest_information[guest].append(meal)


    if command[0] == "Dislike":
        if guest not in guest_information.keys():
            print(f'{guest} is not at the party.')
            command = input().split('-')
            continue
        if meal in guest_information[guest]:
            print(f"{guest} doesn't like the {meal}.")
            guest_information[guest].remove(meal)
            unliked_meals += 1
        else:
            print(f"{guest} doesn't have the {meal} in his/her collection.")


    command = input().split('-')

for key in guest_information.keys():
    print(f'{key}: {", ".join(guest_information[key])}')
print(f'Unliked meals: {unliked_meals}')