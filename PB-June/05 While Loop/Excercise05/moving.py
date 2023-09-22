#user input
width = int(input())
length = int(input())
height = int(input())
volume = width * length * height
luggage = 0

#logic
while luggage < volume:
    moved_luggage = input()
    if moved_luggage == "Done":
        break
    luggage += int(moved_luggage)

difference = abs(volume - luggage)

#print output
if luggage >= volume:
    print(f'No more free space! You need {difference} Cubic meters more.')
else:
    print(f'{difference} Cubic meters left.')








