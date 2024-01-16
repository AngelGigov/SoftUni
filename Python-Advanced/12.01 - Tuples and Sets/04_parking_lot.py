n = int(input())
cars = set()

for i in range(n):
    command, car = input().split(", ")

    if command == "IN":
        cars.add(car)
    elif command == "OUT":
        if car in cars:
            cars.remove(car)

if cars:
    for car in cars:
        print(car)
else:
    print('Parking Lot is Empty')