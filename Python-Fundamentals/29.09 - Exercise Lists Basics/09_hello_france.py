#User Input
items = input().split("|")
budget = int(input())
bought_items = []
sold_items = []


#Logic
for item in items:
    split_item = item.split("->")

    if split_item[0] == "Clothes" and float(split_item[1]) <= 50 and (budget - float(split_item[1])) > 0:
        budget -= float(split_item[1])
        bought_items.append(float(split_item[1]))
    elif split_item[0] == "Shoes" and float(split_item[1]) <= 35.00 and (budget - float(split_item[1])) > 0:
        budget -= float(split_item[1])
        bought_items.append(float(split_item[1]))
    elif split_item[0] == "Accessories" and float(split_item[1]) <= 20.50 and (budget - float(split_item[1])) > 0:
        budget -= float(split_item[1])
        bought_items.append(float(split_item[1]))

#Calculating the sold items
for each in bought_items:
    sold_items.append(round(each * 1.40, 2))

profit = sum(sold_items) - sum(bought_items)


#Print output
print(*sold_items)
print(f'Profit: {profit:.2f}')
if sum(sold_items) + budget > 150:
    print('Hello, France!')
else:
    print("Not enough money.")





