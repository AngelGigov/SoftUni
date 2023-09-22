#user input
screen_type = input()
rows = int(input())
columns = int(input())

income = 0
cinema_volume = rows * columns

#logic
if screen_type == "Premiere":
    income = cinema_volume * 12
elif screen_type == 'Normal':
    income = cinema_volume * 7.50
elif screen_type == 'Discount':
    income = cinema_volume * 5

#print output

print(f'{income:.2f} leva')