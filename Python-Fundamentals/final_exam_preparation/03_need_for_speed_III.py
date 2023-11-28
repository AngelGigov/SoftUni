#User Inputs Number of Cars
number_of_cars = int(input())
car_database = {}

#Get information for the cars
for car in range(number_of_cars):
    car, milage, fuel = input().split("|")
    if car not in car_database.keys():
        car_database[car] =  {"Milage": int(milage), "Fuel": int(fuel)}


command = input().split(" : ")
while command[0] != "Stop":
    if command[0] == "Drive":
        car, distance, needed_fuel = command[1], command[2], command[3]
        if car_database[command[1]]["Fuel"] < int(needed_fuel):
            print("Not enough fuel to make that ride")
        else:
            car_database[command[1]]["Milage"] += int(distance)
            car_database[command[1]]["Fuel"] -= int(needed_fuel)
            print(f'{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.')
            if car_database[command[1]]["Milage"] >= 100000:
                print(f"Time to sell the {car}!")
                car_database.pop(car)

    elif command[0] == "Refuel":
        max_capacity = 75
        car, liters = command[1], command[2]
        if car_database[car]["Fuel"] + int(liters) > max_capacity:
            available_capacity = max_capacity - car_database[car]["Fuel"]
            car_database[car]["Fuel"] += available_capacity
            print(f'{car} refueled with {available_capacity} liters')
        else:
            car_database[car]["Fuel"] += int(liters)
            print(f'{car} refueled with {liters} liters')
    elif command[0] == "Revert":
        car, kilometers = command[1], command[2]
        if (car_database[car]["Milage"] - int(kilometers)) < 10000:
            car_database[car]["Milage"] = 10000
        else:
            car_database[car]["Milage"] -= int(kilometers)
            print(f'{car} mileage decreased by {kilometers} kilometers')

    command = input().split(" : ")

for k in car_database.keys():
    print(f"{k} -> Mileage: {car_database[k]['Milage']} kms, Fuel in the tank: {car_database[k]['Fuel']} lt.")