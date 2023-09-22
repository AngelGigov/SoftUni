
user_input = input()
total_balance = 0

while user_input != "NoMoreMoney":
    user_input = float(user_input)
    if user_input < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {user_input:.2f}')
    total_balance += user_input
    user_input = input()

print(f'Total: {total_balance:.2f}')