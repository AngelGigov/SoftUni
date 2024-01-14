from collections import deque

quantity_of_food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders)) #printing the biggest order

for order in orders.copy():
    if quantity_of_food >= order:
        quantity_of_food -= order
        orders.popleft()
    else:
        print(f'Orders left:', *orders)
        break
else:
    print("Orders complete")