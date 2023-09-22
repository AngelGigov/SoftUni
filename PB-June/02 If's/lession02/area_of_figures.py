from math import pi

#user input
shape = input()
square_size = 0
#logic
if shape == "square":
    side = float(input('Please enter size: '))
    square_size = side * side
elif shape == "rectangle":
    side_a = float(input('Please enter size a: '))
    side_b = float(input('Please enter size b: '))
    square_size = side_a * side_b
elif shape == "circle":
    side_a = float(input('Please enter radius: '))
    square_size = pi * (side_a ** 2)
elif shape == "triangle":
    side_a = float(input('Please enter lenght a: '))
    side_b = float(input('Please enter height b: '))
    square_size = side_a * side_b / 2
else:
    pass
print(f'{square_size:.3f}')
#printout