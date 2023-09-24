#Read User Input
number_of_iterations = int(input())
tank_capacity = 255
liters_poured =  0

#Logic
for i in range(number_of_iterations):
    liters_to_pour = int(input())
    if liters_to_pour > (tank_capacity - liters_poured):
        print('Insufficient capacity!')
        continue
    else:
        liters_poured += liters_to_pour

#Print Output
print(liters_poured)
