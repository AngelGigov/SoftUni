command = ['Pistol', 'Coins', 'Wood', 'Silver', 'Bronze', 'Medallion', 'Cup', 'Gold']
#command = [1, 2, 3, 4, 5, 6, 7, 8]
count = 0
for item in command:
    count += len(item)

print(count)