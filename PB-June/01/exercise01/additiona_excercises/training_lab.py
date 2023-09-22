#Input from user

lenght = float(input())
width = float(input())


centimeter_lenght = lenght * 100
centimeter_width = (width * 100 ) - 100

places_lenght = (centimeter_lenght - (centimeter_lenght % 120)) / 120
places_width = (centimeter_width - (centimeter_width % 70)) / 70

number_of_desks = places_width * places_lenght - 3

print(number_of_desks)
