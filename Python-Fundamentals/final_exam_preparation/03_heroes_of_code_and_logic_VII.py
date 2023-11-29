number_of_heroes = int(input())
heroes = {}

for hero in range(number_of_heroes):
    name, hit_points, mana_points = input().split()
    if int(hit_points) > 100:  #Checking if Hit Point are more that excepted
        hit_points = 100
    if int(mana_points) > 200: #Checking if Mana Point are more that excepted
        mana_points = 200
    if name not in heroes.keys(): #Checking if Hero Exist
        heroes[name] = {"HP": int(hit_points), "MP": int(mana_points)}

command = input().split(" - ")

while command[0] != 'End':

    if command[0] == "CastSpell":
        hero_name = command[1]
        mana_needed = int(command[2])
        spell_name = command[3]
        if heroes[hero_name]["MP"] >= mana_needed:
            heroes[hero_name]["MP"] -= mana_needed
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]["MP"]} MP!')
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command[0] =="TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        if heroes[hero_name]["HP"] - damage > 0:
            heroes[hero_name]["HP"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            heroes.pop(hero_name)

    elif command[0] =="Recharge":
        hero_name = command[1]
        amount = int(command[2])
        if heroes[hero_name]["MP"] + amount > 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")
            heroes[hero_name]["MP"] = 200
        else:
            heroes[hero_name]["MP"] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif command[0] =="Heal":
        hero_name = command[1]
        amount = int(command[2])
        if heroes[hero_name]["HP"] + amount > 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += amount
            print(f"{hero_name} healed for {amount} HP!")

    command = input().split(" - ")

for el in heroes.keys():
    print(f"{el}\n  HP: {heroes[el]['HP']}\n  MP: {heroes[el]['MP']}")
