#User Input
num = int(input())
numbers = []
filtered = []

#Logic
for i in range(num):
    get_num = int(input())
    numbers.append(get_num)

command = input()

if command == 'even':
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)
elif command == 'odd':
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)
elif command == 'negative':
    for number in numbers:
        if number < 0:
            filtered.append(number)
elif command == 'positive':
    for number in numbers:
        if number >= 0:
            filtered.append(number)

#Print Output
print(filtered)