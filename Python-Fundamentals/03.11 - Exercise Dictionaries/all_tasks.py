# 1
symbols = [character for character in input() if character != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters.keys():  # if symbol not in letters
        letters[symbol] = 0
    letters[symbol] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")

# 2

resources = {}
while True:
    current_resources = input()
    if current_resources == "stop":
        break
    current_quantity = int(input())
    if current_resources not in resources.keys():  # if current_resources not in resources
        resources[current_resources] = 0
    resources[current_resources] += current_quantity
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")

# 3

countries = input().split(", ")
capitals = input().split(", ")
# final_information = {countries[index]: capitals[index]
#                      for index in range(len(countries))}
final_information = dict(zip(countries, capitals))
for country, capital in final_information.items():
    print(f"{country} -> {capital}")

# 4

phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, phone_number = entry.split("-")
    phonebook[name] = phone_number
searches = int(entry)
for search in range(searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")

# 5

items = {"shards": 0, "fragments": 0, "motes": 0}
obtained = False
while not obtained:
    current_items = input().split()
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
for material, quantity in items.items():
    print(f"{material}: {quantity}")

# 11

force_side_dictionary = {}
command = input()
while command != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        user_is_part_of_the_force = False
        for value in force_side_dictionary.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_side_dictionary.keys():
                force_side_dictionary[force_side] = []
            force_side_dictionary[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for value in force_side_dictionary.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_side_dictionary.keys():
            force_side_dictionary[force_side] = []
        force_side_dictionary[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for force_side, force_users in force_side_dictionary.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for force_user in force_users:
            print(f"! {force_user}")







