command = input()
stock = {}
while command != 'statistics':
    product, qty = command.split(': ')
    if product not in stock.keys():
        stock[product] = int(qty)
    else:
        stock[product] += int(qty)
    command = input()

print("Products in stock:")
for product, quantity in stock.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(stock.keys())}")
print(f"Total Quantity: {sum(stock.values())}")