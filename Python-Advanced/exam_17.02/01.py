from collections import deque


money = [int(x) for x in input().split()]
foods = deque([int(x) for x in input().split()])

count = 0

while money and foods:
    current_money = money[-1]
    current_food = foods[0]

    if current_money == current_food:
        count += 1
        money.pop()
        foods.popleft()
    elif current_money > current_food:
        count += 1
        money.pop()
        foods.popleft()
        if len(money) > 0:
            money[-1] += abs(current_money - current_food)

    else:
        money.pop()
        foods.popleft()

if count >= 4:
    print(f'Gluttony of the day! Henry ate {count} foods.')
elif 0 < count < 4:
    if count == 1:
        print(f'Henry ate: {count} food.')
    else:
        print(f'Henry ate: {count} foods.')
else:
    print(f'Henry remained hungry. He will try next weekend again.')