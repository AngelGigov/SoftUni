travel_route = input().split('||')
fuel_amount = int(input())
ammunition_amount = int(input())

traveled_years = 0

for command in travel_route:
    instructions = command.split()
    if instructions[0] == 'Titan':
        print("You have reached Titan, all passengers are safe.")

    elif instructions[0] == "Travel":
        light_years = int(instructions[1])
        if fuel_amount - light_years < 0:
            print("Mission failed.")
            break #exit()?
        else:
            fuel_amount -= light_years
            traveled_years += light_years
            print(f"The spaceship travelled {light_years} light-years.")

    elif instructions[0] == "Enemy": #Fight or Run
        enemy_point = int(instructions[1])
        if ammunition_amount >= enemy_point: #Fight situation
            ammunition_amount -= enemy_point
            print(f"An enemy with {enemy_point} armour is defeated.")
        else: # Run situation
            if enemy_point * 2 < fuel_amount:
                fuel_amount -= enemy_point * 2
                print(f"An enemy with {enemy_point} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break #exit()
    elif instructions[0] == "Repair":
        number = int(instructions[1])
        ammunition_amount += number * 2
        print(f"Ammunitions added: {number * 2}.")
        fuel_amount += number
        print(f"Fuel added: {number}.")



