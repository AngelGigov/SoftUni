goal = 10000
steps_walked_today = 0

while steps_walked_today < goal:
    steps_today = input()
    if steps_today == 'Going home':
        last_steps = int(input())
        steps_walked_today += last_steps
        break
    steps = int(steps_today)
    steps_walked_today += steps
difference = abs(goal - steps_walked_today)

#print output
if steps_walked_today >= goal:
    print('Goal reached! Good job!')
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")



