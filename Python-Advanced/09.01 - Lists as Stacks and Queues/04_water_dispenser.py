from collections import deque

liters_of_water = int(input())

line = deque()

name = input()
while name != "Start":
    line.append(name)
    name = input()

command = input()
while command != "End":
    data = command.split()
    if len(data) == 1:
        if liters_of_water >= int(data[0]):
            liters_of_water -= int(data[0])
            print(f'{line.popleft()} got water')
        else:
            print(f'{line.popleft()} must wait')

    elif len(data) == 2:
        liters_of_water += int(data[1])

    command = input()

print(f'{liters_of_water} liters left')

