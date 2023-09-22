# User input
cotrole_in_minutes = int(input())
control_in_seconds = int(input())
lenght = float(input())
time_for_100_meters = int(input())

# Logic
controle_time = cotrole_in_minutes * 60 + control_in_seconds
improvment_of_time = (lenght / 120) * 2.5
competitor_time = lenght / 100 * time_for_100_meters - improvment_of_time

# Print output
if competitor_time <= controle_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f'His time is {competitor_time:.3f}.')
else:
    difference = abs(competitor_time - controle_time)
    print(f'No, Marin failed! He was {difference:.3f} second slower.')

