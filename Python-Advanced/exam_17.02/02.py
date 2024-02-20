n = int(input())

matrix = []
possition = []
armour = 300
number_of_enemies = 4

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(list(input()))

    if "J" in matrix[row]:
        possition = [row, matrix[row].index("J")]
        matrix[row][possition[1]] = '-'


command = input()
while True:
    current_row_index, current_col_index = possition
    row_movement, col_movement = directions[command]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    symbol = matrix[desired_row_index][desired_col_index]
    matrix[desired_row_index][desired_col_index] = "J"
    matrix[current_row_index][current_col_index] = '-'
    possition = [desired_row_index, desired_col_index]

    if symbol == "E":
        armour -= 100
        number_of_enemies -= 1
        if number_of_enemies <= 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        if armour <= 0:
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{possition[0]}, {possition[1]}]!")
            break
    elif symbol == "R":
        armour = 300

    command = input()

print(*[''.join(row) for row in matrix], sep='\n')

