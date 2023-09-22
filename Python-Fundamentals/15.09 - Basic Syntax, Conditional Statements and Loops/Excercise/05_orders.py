#User input
number_of_orders = int(input())
total_price = 0
#Logic

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if not 0.01 <= price_per_capsule <= 100.00 or not 1 <= days <= 31 or not 1 <= capsules <= 2000:
        continue
    else:
        price = capsules * price_per_capsule * days
        print(f'The price for the coffee is: ${price:.2f}')
        total_price += price
print(f'Total: ${total_price:.2f}')
