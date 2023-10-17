people_waiting = int(input())
lift_wagons = [int(x) for x in input().split()]

for wagon, element in enumerate(lift_wagons):
    wagon_capacity = 4 - element
    if people_waiting >= 4:
        lift_wagons[wagon] += wagon_capacity
        people_waiting -= wagon_capacity
    else:
        lift_wagons[wagon] += people_waiting
        people_waiting = 0

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
elif len([cart for cart in lift_wagons if cart < 4]) > 0:
    print(f"The lift has empty spots!")

print(' '.join(map(str,lift_wagons)))
