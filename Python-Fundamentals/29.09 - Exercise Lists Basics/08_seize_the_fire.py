#User input
fire_input = input().split('#') #Splitting the string into individual fires
water = int(input()) #Amount of water we receive
effort = 0
total_fire = 0
cells = []

#Spliting the fire_input into indivitual fires
for i in fire_input:

    individual_fire = i.split(" = ")

    if water <= total_fire + int(individual_fire[1]): #We are skipping a loop if ran out of water
        continue
    if individual_fire[0] == 'Low' and 0 < int(individual_fire[1]) <= 50:
        total_fire += int(individual_fire[1])
        effort += int(individual_fire[1]) * 0.25
        cells.append(individual_fire[1])
    elif individual_fire[0] == 'Medium' and 50 < int(individual_fire[1]) <= 80:
        total_fire += int(individual_fire[1])
        effort += int(individual_fire[1]) * 0.25
        cells.append(individual_fire[1])
    elif individual_fire[0] == 'High' and 80 < int(individual_fire[1]) <= 125: #This can be else
        total_fire += int(individual_fire[1])
        effort += int(individual_fire[1]) * 0.25
        cells.append(individual_fire[1])



#Print Output
print("Cells:")
for i in cells:
    print(f" - {i}")
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')