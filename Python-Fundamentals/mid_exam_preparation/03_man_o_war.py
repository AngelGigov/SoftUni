def status_of_ship(ship, max_health):
    sections_that_need_repair = 0
    for el in ship:
        if el < max_health * 0.2:
            sections_that_need_repair += 1
    print(f"{sections_that_need_repair} sections need repair.")

def ship_status(pirate_ship, warship):
    status_pirate_ship = sum(pirate_ship)
    status_warship_ship = sum(warship)
    print(f"Pirate ship status: {status_pirate_ship}\nWarship status: {status_warship_ship}")

#  User Input
pirate_ship_status = [int(x) for x in input().split(">")]
battle_ship_status = [int(x) for x in input().split(">")]
maximum_health_capacity = int(input())

command = input().split()

while command[0] != 'Retire':

    if command[0] == 'Fire': #Pirate ship attack
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(battle_ship_status): #checking if index is valid
            battle_ship_status[index] -= damage
            if battle_ship_status[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit() # Quit the program as you win
    elif command[0] == 'Defend': #Pirate ship defens
        start = int(command[1])
        end = int(command[2])
        damage = int(command[3])
        if 0 <= start < len(pirate_ship_status) and 0 <= end < len(pirate_ship_status): #checking if both indexes are valid
            for el in range(start, end + 1):
                pirate_ship_status[el] -= damage
                if pirate_ship_status[el] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit() #Quit as you lose
    elif command[0] == 'Repair': # Repair Pirate ship
        index = int(command[1])
        health = int(command[2])
        if pirate_ship_status[index] + health <= maximum_health_capacity:
            pirate_ship_status[index] += health
        else:
            pirate_ship_status[index] += maximum_health_capacity - pirate_ship_status[index]
    elif command[0] == 'Status':
        status_of_ship(pirate_ship_status, maximum_health_capacity)


    command = input().split()

ship_status(pirate_ship_status, battle_ship_status)
