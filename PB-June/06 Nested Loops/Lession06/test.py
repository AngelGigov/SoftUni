
# Read user input
number_of_days = int(input())
food_qty = float(input())
total_food_eaten_by_dog = 0
total_food_eaten_by_cat = 0
total_eaten_bescuits = 0


# Logic
for i in range(1, number_of_days + 1):
    eaten_food_by_dog = int(input())
    eaten_food_by_cat = int(input())
    total_food_eaten_by_dog += eaten_food_by_dog
    total_food_eaten_by_cat += eaten_food_by_cat
    if i % 3 == 0:
        eaten_biscuits = (eaten_food_by_dog + eaten_food_by_cat) * 0.1
        total_eaten_bescuits += eaten_biscuits

# counting percenteges
percentage_of_dog_eaten_food = (total_food_eaten_by_dog / (total_food_eaten_by_dog + total_food_eaten_by_cat)) * 100
percentage_of_cat_eaten_food = (total_food_eaten_by_cat / (total_food_eaten_by_dog + total_food_eaten_by_cat)) * 100
percentage_of_total_eaten_food = ((total_food_eaten_by_dog + total_food_eaten_by_cat) / food_qty) * 100

# Print output
print(f'Total eaten biscuits: {round(total_eaten_bescuits)}gr.')
print(f'{percentage_of_total_eaten_food:.2f}% of the food has been eaten.')
print(f'{percentage_of_dog_eaten_food:.2f}% eaten from the dog.')
print(f'{percentage_of_cat_eaten_food:.2f}% eaten from the cat.')



