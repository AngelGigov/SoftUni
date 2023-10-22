#User Input
days_of_the_adventure = int(input())
players = int(input())
group_energy = float(input())
water_for_day = float(input()) # This is for person - needs to be calculated for group
food_per_day = float(input())  # This is for person - needs to be calculated for group

not_enough_energy = False

total_water_for_group = players * water_for_day * days_of_the_adventure
total_food_for_group = players * food_per_day * days_of_the_adventure


for day in range(1, days_of_the_adventure + 1):
    energy_lost = float(input()) #wood chopping
    group_energy -= energy_lost
    if group_energy <= 0:
        not_enough_energy = True
        print(f"You will run out of energy. You will be left with {total_food_for_group:.2f} food and {total_water_for_group:.2f} water.")
        break
    if day % 2 == 0: # Drink water
        group_energy *= 1.05
        total_water_for_group *= 0.7
    if day % 3 == 0: # Eating
        total_food_for_group -= total_food_for_group / players
        group_energy *= 1.1

#Print Output
if not_enough_energy == False:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")