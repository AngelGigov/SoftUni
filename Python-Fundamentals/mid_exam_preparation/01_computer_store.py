total_taxes = 0
total_price = 0
is_discount = False

command = input()
while command != 'special' and command != 'regular':
    command_to_float = float(command)
    if command_to_float <= 0:
        print('Invalid price!')
        command = input()
        continue
    price = command_to_float
    tax = price * 0.2
    total_price += price
    total_taxes += tax

    command = input()

if command == 'special':
    is_discount = True

if total_price <= 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {total_taxes:.2f}$")
    print("-----------")
    if is_discount:
        print(f"Total price: {(total_price + total_taxes)*0.9:.2f}$")
    else:
        print(f"Total price: {total_price + total_taxes:.2f}$")


