from math import ceil, floor

#user input

days_missing = int(input())
left_food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turt_food_gr = float(input())

#Logic

dog_needed = days_missing * dog_food_kg
cat_needed = days_missing * cat_food_kg
turt_needed = days_missing * turt_food_gr / 1000

all_food_needed = dog_needed + cat_needed + turt_needed

#User output

if all_food_needed < left_food_kg:
    leftover = abs(all_food_needed - left_food_kg)
    print(f'{floor(leftover)} kilos of food left.')
else:
    need_more_food = abs(left_food_kg - all_food_needed)
    print(f'{ceil(need_more_food)} more kilos of food are needed.')
