# User Input
number_of_locations = int(input())

output_for_the_day = 0


# Logic
for location in range(number_of_locations):
    expected_average_output = float(input())
    day_of_mining = int(input())
    for day in range(day_of_mining):
        mining_output_for_day = int(input())
        output_for_the_day += mining_output_for_day

    average_for_the_day = output_for_the_day / day_of_mining

    if average_for_the_day >= expected_average_output:
        print(f'Good job! Average gold per day: {average_for_the_day:.2f}.')
    else:
        difference = abs(expected_average_output - average_for_the_day)
        print(f'You need {difference:.2f} gold.')

    output_for_the_day = 0