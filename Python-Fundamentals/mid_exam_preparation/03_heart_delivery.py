user_input = input().split('@')
neighborhood = [int(x) for x in user_input]

cupid_current_possition = 0

command = input()

while command != 'Love!':
    jump, lenght = command.split()
    cupid_current_possition += int(lenght)
    if cupid_current_possition > len(neighborhood) - 1:
        cupid_current_possition = 0
    if neighborhood[cupid_current_possition] == 0:
        print(f"Place {cupid_current_possition} already had Valentine's day.")
    else:
        neighborhood[cupid_current_possition] -= 2
        if neighborhood[cupid_current_possition] == 0:
            print(f"Place {cupid_current_possition} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {cupid_current_possition}.")
count_successful_houses = [el for el in neighborhood if el == 0]
if len(count_successful_houses) == len(neighborhood):
    print("Mission was successful.")
else:
    print(f'Cupid has failed {len(neighborhood) - len(count_successful_houses)} places.')



