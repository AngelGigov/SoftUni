# User Input
tshirt_price = float(input())
total_to_win_ball = float(input())

# Logic
shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.2
shoes_price = (tshirt_price + shorts_price) * 2

total_after_discount = (tshirt_price + shorts_price + socks_price + shoes_price) * 0.85

#print output
if total_after_discount >= total_to_win_ball:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_after_discount:.2f} lv.')
else:
    difference = abs(total_to_win_ball - total_after_discount)
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {difference:.2f} lv. more.')