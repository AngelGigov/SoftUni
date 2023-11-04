products = input().split()
stock = {}

for i in range(0, len(products), 2):
    product = products[i]
    qty = products[i + 1]
    stock[product] = int(qty)

products_to_search = input().split()

for element in products_to_search:
    if element in stock.keys():
        print(f"We have {stock[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")