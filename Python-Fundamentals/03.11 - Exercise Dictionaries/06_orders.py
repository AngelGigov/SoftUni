inventory = {}

command = input()
while command != 'buy':
    product, price, qty = command.split()
    if product not in inventory:
        inventory[product] = [float(price), int(qty)]
    else:
        inventory[product][0] = float(price)
        inventory[product][1] += int(qty)

    command = input()

for key, value in inventory.items():
    print(f"{key} -> {inventory[key][0] * inventory[key][1]:.2f}")