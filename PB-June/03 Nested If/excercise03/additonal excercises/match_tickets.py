#user input
budget = float(input())
category = input()
people = int(input())

transport = 0
tickets_price = 0

#Logic
if 1 <= people <= 4:
    if category == "VIP":
        transport = budget * 0.75
        tickets_price = people * 499.99
    elif category == 'Normal':
        transport = budget * 0.75
        tickets_price = people * 249.99
elif 5 <= people <= 9:
    if category == "VIP":
        transport = budget * 0.6
        tickets_price = people * 499.99
    elif category == 'Normal':
        transport = budget * 0.6
        tickets_price = people * 249.99
elif 10 <= people <= 24:
    if category == "VIP":
        transport = budget * 0.5
        tickets_price = people * 499.99
    elif category == 'Normal':
        transport = budget * 0.5
        tickets_price = people * 249.99
elif 25 <= people <= 49:
    if category == "VIP":
        transport = budget * 0.4
        tickets_price = people * 499.99
    elif category == 'Normal':
        transport = budget * 0.4
        tickets_price = people * 249.99
elif  people > 50:
    if category == "VIP":
        transport = budget * 0.25
        tickets_price = people * 499.99
    elif category == 'Normal':
        transport = budget * 0.25
        tickets_price = people * 249.99


total = transport + tickets_price
difference = abs(budget - total)

#print output

if budget > total:
    print(f'Yes! You have {difference:.2f} leva left.')
else:
    print(f'Not enough money! You need {difference:.2f} leva.')

