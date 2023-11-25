# 1
stops = input()
command = input().split(":")
while command[0] != "Travel":
    if command[0] == "Add Stop":
        index, some_string = int(command[1]), command[2]
        if index in range(len(stops)):
            stops = stops[:index] + some_string + stops[index:]
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            stops = stops[:start_index] + stops[end_index + 1:]
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
    command = input().split(":")
print(f"Ready for world tour! Planned stops: {stops}")


# 1.1 - functions

def add_stop(stops, index, some_string):
    if index in range(len(stops)):
        stops = stops[:index] + some_string + stops[index:]
    return stops


def remove_stop(stops, start_index, end_index):
    if start_index in range(len(stops)) and end_index in range(len(stops)):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch(stops, old_string, new_string):
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


stops = input()
command = input().split(":")
while command[0] != "Travel":
    if command[0] == "Add Stop":
        index, some_string = int(command[1]), command[2]
        stops = add_stop(stops, index, some_string)
    elif command[0] == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        stops = remove_stop(stops, start_index, end_index)
    elif command[0] == "Switch":
        old_string, new_string = command[1], command[2]
        stops = switch(stops, old_string, new_string)
    print(stops)
    command = input().split(":")
print(f"Ready for world tour! Planned stops: {stops}")

# 2

import re

information = input()
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
# index 1 - item name, index 3 - expiration date, index 5 - calories
matches = re.findall(pattern, information)
total_calories = sum([int(match[5]) for match in matches])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for element in matches:
    item_name = element[1]
    expiration_date = element[3]
    calories = element[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

# 3
cities = {}
# Collecting cities information
command = input().split("||")
while command[0] != "Sail":
    city, population, gold = command[0], int(command[1]), int(command[2])
    if city not in cities.keys():
        cities[city] = {"population": 0, "gold": 0}
        # {"Tortuga": {"population": 0, "gold": 0}}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input().split("||")
# Doing events
command = input().split("=>")
while command[0] != "End":
    action = command[0]
    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town, gold = command[1], int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input().split("=>")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town, town_information in cities.items():
        print(f'{town} -> Population: {town_information["population"]} citizens, Gold: {town_information["gold"]} kg')
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
