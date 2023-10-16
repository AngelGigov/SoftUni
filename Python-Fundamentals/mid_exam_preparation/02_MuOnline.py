health = 100
bitcoins = 0
rooms = input().split('|')

is_killed = False

for number, room in enumerate(rooms):
    command, value = room.split()

    if command == "potion":
        if health + int(value) > 100:
            print(f'You healed for {100 - health} hp.')
            health += 100 - health
        else:
            health += int(value)
            print(f'You healed for {value} hp.') #This should be changed as you can't heal more than 100
        if health > 100:
            health = 100
        print(f'Current health: {health} hp.')
    elif command == "chest":
        bitcoins += int(value)
        print(f'You found {value} bitcoins.')
    else:
        health -= int(value)
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f'Best room: {number + 1}')
            is_killed = True
            break
        else:
            print(f"You slayed {command}.")

if is_killed != True:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

