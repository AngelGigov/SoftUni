#User input
number_of_cats = int(input())

total_eaten = 0

group_one = 0    # small cats 100 <= food < 200
group_two = 0    # big cats   200 <= food < 300
group_tree = 0   # huge cats  300 <= food < 400

# Logic
for cat in range(number_of_cats):
    food = float(input())
    total_eaten += food
    if 100 <= food < 200:
        group_one += 1
    elif 200 <= food < 300:
        group_two += 1
    elif 300 <= food < 400:
        group_tree += 1

total_price = (total_eaten / 1000) * 12.45

#Print output
print(f'Group 1: {group_one} cats.')
print(f'Group 2: {group_two} cats.')
print(f'Group 3: {group_tree} cats.')
print(f'Price for food per day: {total_price:.2f} lv.')