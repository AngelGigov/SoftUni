side_one = float(input())
side_two = float(input())
height = float(input())

area = (side_one + side_two) * height / 2
formatted_area = "{:.2f}".format(area)

print(formatted_area)