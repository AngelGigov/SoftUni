#user input
budget = float(input())
season = input()

price = 0
location = ''
place_of_accomodation = ''


#logic
if budget <= 1000:
    place_of_accomodation = "Camp"
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    place_of_accomodation = "Hut"
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
elif budget > 3000:
    place_of_accomodation = "Hotel"
    price = budget * 0.9
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'

#print output
print(f'{location} - {place_of_accomodation} - {price:.2f}')