def orders(type_of_drink, qty):
    if type_of_drink == 'coffee':
        return f'{qty * 1.50:.2f}'
    elif type_of_drink == 'water':
        return f'{qty * 1.00:.2f}'
    elif type_of_drink == 'coke':
        return f'{qty * 1.40:.2f}'
    elif type_of_drink == 'snacks':
        return f'{qty * 2.00:.2f}'

drink = input()
number = int(input())

print(orders(drink, number))
