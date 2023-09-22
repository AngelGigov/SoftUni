from math import floor, ceil

#User input
squere_M = int(input())
grape_per_m = float(input())
needed_wine_liters = int(input())
workers_needed = int(input())

#logic
grape_harvest = squere_M * grape_per_m
wine_produced = grape_harvest * 0.4 / 2.5

leftover_wine = ceil(wine_produced - needed_wine_liters)
missing_wine = floor(needed_wine_liters - wine_produced)
wine_per_capita = ceil(leftover_wine / workers_needed)



#user output
if wine_produced >= needed_wine_liters:
    print(f'Good harvest this year! Total wine: {int(wine_produced)} liters.')
    print(f'{leftover_wine} liters left -> {wine_per_capita} liters per person.')

else:
    print(f'It will be a tough winter! More {missing_wine} liters wine needed.')