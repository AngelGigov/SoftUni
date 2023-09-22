#user input
bought_food_in_kg = int(input())
bought_food_in_grams = bought_food_in_kg * 1000
given_food_total = 0
# logic
command = input()
while command != "Adopted":
    given_food = int(command)
    given_food_total += given_food
    command = input()

difference = abs(bought_food_in_grams - given_food_total)
#print output
if bought_food_in_grams >= given_food_total:
    print(f'Food is enough! Leftovers: {difference} grams.')
else:
    print(f'Food is not enough. You need {difference} grams more.')


