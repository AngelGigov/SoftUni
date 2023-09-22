#User input
dessert = input()
number_of_deserts = int(input())
day = int(input())

total = 0

if day <= 15:
    if dessert == "Cake":
        total = number_of_deserts * 24
    elif dessert == "Souffle":
        total = number_of_deserts * 6.66
    elif dessert == "Baklava":
        total = number_of_deserts * 12.60
else:
    if dessert == "Cake":
        total = number_of_deserts * 28.70
    elif dessert == "Souffle":
        total = number_of_deserts * 9.80
    elif dessert == "Baklava":
        total = number_of_deserts * 16.98

# Discounts
if day <= 22 and 100 <= total <= 200:
    total *= 0.85
elif day <= 22 and total > 200:
    total *= 0.75

if day <= 15:
    total *= 0.9

print(f'{total:.2f}')