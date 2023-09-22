#user input
season = input()
km_per_month = float(input())

salary = 0

#logic
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.75) * 4
    elif season == "Summer":
        salary = (km_per_month * 0.9) * 4
    elif season == "Winter":
        salary = (km_per_month * 1.05) * 4
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        salary = (km_per_month * 0.95) * 4
    elif season == "Summer":
        salary = (km_per_month * 1.10) * 4
    elif season == "Winter":
        salary = (km_per_month * 1.25) * 4
elif 10000 < km_per_month <= 20000:
    salary = (km_per_month * 1.45) * 4

gross_salary = salary - (salary * 0.1)

#print output
print(f'{gross_salary:.2f}')
