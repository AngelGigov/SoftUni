from collections import deque

initial_fuel = [int(x) for x in input().split()]
cosumption_index = deque([int(x) for x in input().split()])
ammount_of_fuel_needed = [int(x) for x in input().split()]

altitute_reached = 0
reached_top = False

while initial_fuel or cosumption_index:
    current_fuel = initial_fuel[-1]
    current_consumption = cosumption_index[0]

    if current_fuel - current_consumption >= ammount_of_fuel_needed[0]:
        altitute_reached += 1
        print(f'John has reached: Altitude {altitute_reached}')
        initial_fuel.pop()
        cosumption_index.popleft()
        ammount_of_fuel_needed.pop()
    else:
        print(f"John did not reach: Altitude {altitute_reached + 1}")
        break

    if len(initial_fuel) == 0:
        reached_top = True

if not reached_top:
    print(f"John failed to reach the top. Reached altitudes: {[print(f'Altitude {i}') for i in range(1, altitute_reached + 1)]}")
