#user input
chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()


bouquet = 0

#logic prices
if season == "Spring" or season == 'Summer':
    sum_chrusantem = chrysanthemums * 2.00
    sum_roses = roses * 4.10
    sum_tulips = tulips * 2.50
    bouquet = sum_chrusantem + sum_roses + sum_tulips
    if holiday == 'Y':
        bouquet *= 1.15
elif season == "Autumn" or season == "Winter":
    sum_chrusantem = chrysanthemums * 3.75
    sum_roses = roses * 4.50
    sum_tulips = tulips * 4.15
    bouquet = sum_chrusantem + sum_roses + sum_tulips
    if holiday == 'Y':
        bouquet *= 1.15

#logic discounts
if season == "Spring" and tulips > 7: #there is discount during the "Sprint" for over 7 tulups
    bouquet *= 0.95
elif season == "Winter" and roses >= 10: #there is discount during Winter for 10 and more roses
    bouquet *= 0.9

if chrysanthemums + roses + tulips > 20:
    bouquet *= 0.8

bouquet = bouquet + 2 #price for arrange

#print out the how much cost bouquet
print(f'{bouquet:.2f}')
