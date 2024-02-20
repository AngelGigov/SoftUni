size = int(input())



fishing_area = []
boat_position = []
collected_fish = 0


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    fishing_area.append(list(input()))

    if "S" in fishing_area[row]:
        boat_position = [row, fishing_area[row].index("S")]

command = input()
while command != "collect the nets":

    current_row = boat_position[0] + directions[command][0]
    if current_row > size - 1:
        current_row = 0
    elif current_row < 0:
        current_row = size - 1
    current_col = boat_position[1] + directions[command][1]
    if current_col > size - 1:
        current_col = 0
    elif current_col < 0:
        current_col = size - 1

    boat_position = [current_row, current_col]
    possition = fishing_area[current_row][current_col]
    fishing_area[current_row][current_col] = '-'

    if possition == "W":
        print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{boat_position[0]},{boat_position[1]}]')
        exit()

    if possition.isdigit():
        collected_fish += int(possition)


    command = input()

if collected_fish >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f'Amount of fish caught: {collected_fish} tons.')

[print(*i) for i in fishing_area]