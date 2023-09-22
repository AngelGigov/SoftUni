#user input
type_of_fuel = input().lower()
liters_of_fuel = int(input())

possible_fuels = ['gasoline', 'diesel', 'gas']

if type_of_fuel in possible_fuels:
    if liters_of_fuel < 25:
        print(f'Fill your tank with {type_of_fuel}!')
    else:
        print(f'You have enough {type_of_fuel}.')
else:
    print("Invalid fuel!")