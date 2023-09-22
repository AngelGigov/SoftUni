
# User input
number_of_balls = int(input())
points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
other_balls = 0
black_balls = 0


# Logic
for i in range(number_of_balls):
    colour = input()
    if colour == 'red':
        red_balls += 1
        points += 5
    elif colour == 'orange':
        orange_balls += 1
        points += 10
    elif colour == 'yellow':
        yellow_balls += 1
        points += 15
    elif colour == 'white':
        white_balls += 1
        points += 20
    elif colour == 'black':
        black_balls += 1
        points = points // 2
    else:
        other_balls += 1
        continue

#print output
print(f"Total points: {points}")
print(f"Red balls: {red_balls}")
print(f"Orange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}")
print(f"White balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
