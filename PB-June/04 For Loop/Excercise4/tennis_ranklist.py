#user input
number_of_tornaments = int(input())
start_points = int(input())
total_points = 0
tournament_won = 0

for tournament in range(number_of_tornaments):
    stage = input()
    if stage == "W":
        total_points += 2000
        tournament_won += 1
    elif stage == "F":
        total_points += 1200
    elif stage == "SF":
        total_points += 720

average_points = total_points // number_of_tornaments
total_points += start_points
percentage_of_won_tournaments = tournament_won / number_of_tornaments * 100

#print output
print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{percentage_of_won_tournaments:.2f}%')
