# Read user input
product = input()
town = input()
qty = float(input())

total = 0

# Logical
if town == 'Sofia':
    if product == 'coffee':
        total = qty * 0.5
    elif product == 'water':
        total = qty * 0.8
    elif product == 'beer':
        total = qty * 1.2
    elif product == 'sweets':
        total = qty * 1.45
    elif product == 'peanuts':
        total = qty * 1.6

elif town == 'Plovdiv':
    if product == 'coffee':
        total = qty * 0.4
    elif product == 'water':
        total = qty * 0.7
    elif product == 'beer':
        total = qty * 1.15
    elif product == 'sweets':
        total = qty * 1.3
    elif product == 'peanuts':
        total = qty * 1.5

elif town == 'Varna':
    if product == 'coffee':
        total = qty * 0.45
    elif product == 'water':
        total = qty * 0.7
    elif product == 'beer':
        total = qty * 1.1
    elif product == 'sweets':
        total = qty * 1.35
    elif product == 'peanuts':
        total = qty * 1.55

# print output
print(total)