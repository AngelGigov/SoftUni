#user input
lili_age = int(input())
laundry_price = float(input())
toy_price = int(input())
total_toys = 0
total_money = 0
current_birthday_money = 0

#logic
for birthday in range(1, lili_age + 1):
    if birthday % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toys += 1

total_money += total_toys * toy_price
difference = abs(total_money - laundry_price)

#print output
if total_money >= laundry_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')

