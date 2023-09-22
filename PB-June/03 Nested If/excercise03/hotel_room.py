#user input
month = input()
days = int(input())

studio_price = 0
apartment_price = 0


#logic
if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 7 < days <= 14:
        studio_price *= 0.95
    elif days > 14:
        studio_price *= 0.7
        apartment_price *= 0.9

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if days > 14:
        studio_price *= 0.8
        apartment_price *= 0.9

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if days > 14:
        apartment_price *= 0.9

apartment_vacation = days * apartment_price
studio_vacation = days * studio_price

#Print output
print(f'Apartment: {apartment_vacation:.2f} lv.')
print(f'Studio: {studio_vacation:.2f} lv.')



#discount to be calculated




#print output