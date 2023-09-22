#User input
budget = float(input())
season = input()

destination = ''
place_vacation = ''

#logic
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        place_vacation = "Camp"
    elif season == "winter":
        budget *= 0.7
        place_vacation = "Hotel"
elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
        place_vacation = "Camp"
    elif season == "winter":
        budget *= 0.8
        place_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    place_vacation = "Hotel"
    budget *= 0.9

#Print output
print(f'Somewhere in {destination}')
print(f'{place_vacation} - {budget:.2f}')