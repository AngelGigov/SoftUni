#user input
budget = int(input())
season = input()
fisherman_count = int(input())
ship_price = 0

#logic
if season == "Spring":
    ship_price = 3000
    if 0 < fisherman_count <= 6:
        ship_price *= 0.9
    elif 7 <= fisherman_count <=11:
        ship_price *= 0.85
    elif fisherman_count > 12:
        ship_price *= 0.75
elif season == "Summer" or season == 'Autumn':
    ship_price = 4200
    if 0 < fisherman_count <= 6:
        ship_price *= 0.9
    elif 7 <= fisherman_count <=11:
        ship_price *= 0.85
    elif fisherman_count > 12:
        ship_price *= 0.75
elif season == "Winter": #this could be else
    ship_price = 2600
    if 0 < fisherman_count <= 6:
        ship_price *= 0.9
    elif 7 <= fisherman_count <=11:
        ship_price *= 0.85
    elif fisherman_count > 12:
        ship_price *= 0.75

#additional discount
if fisherman_count % 2 == 0 and not season == 'Autumn':
    ship_price *= 0.95

difference = abs(ship_price - budget)

#print output
if budget >= ship_price:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')
