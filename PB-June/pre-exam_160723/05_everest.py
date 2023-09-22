# User input
base_camp = 5364
summit = 8848
max_days = 5
is_climbed = False

total_days = 1
current_height = base_camp

command = input()
while command != "END":
    climbed_meters = int(input())
    if command == "Yes":
        total_days += 1
        if total_days > 5:
            break
    base_camp += climbed_meters
    if base_camp >= summit:
        is_climbed = True
        break
    command = input()

if is_climbed:
    print(f'Goal reached for {total_days} days!')
else:
    print('Failed!')
    print(f'{base_camp}')
