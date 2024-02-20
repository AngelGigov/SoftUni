n = int(input())

matrix = []
possition = []
amount = 100
won_jackpot = False0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    matrix.append(list(input()))

    if "G" in matrix[row]:
        possition = [row, matrix[row].index("G")]
        matrix[row][possition[1]] = '-' # clearing the possition of the Gambler


command = input()
while command != 'end':
    current_row_index, current_col_index = possition
    row_movement, col_movement = directions[command]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    if (desired_row_index < 0 or desired_row_index >= len(matrix)) or (desired_col_index < 0 or desired_col_index >= len(matrix)):
        print('Game over! You lost everything!')
        exit()

    symbol = matrix[desired_row_index][desired_col_index]
    matrix[desired_row_index][desired_col_index] = "G"
    matrix[current_row_index][current_col_index] = '-'
    possition = [desired_row_index, desired_col_index]

    if symbol == "W":
        amount += 100
    elif symbol == "P":
        amount -= 200
        if amount <= 0:
            print('Game over! You lost everything!')
            exit()
    elif symbol == "J":
        won_jackpot = True
        amount += 100000
        break

    command = input()

if won_jackpot:
    print("You win the Jackpot!")

print(f'End of the game. Total amount: {amount}$')
print(*[''.join(row) for row in matrix], sep='\n')

