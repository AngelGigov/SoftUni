#User inputs
days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

#Logic
for day in range(1, days + 1):

    total_plunder += daily_plunder

    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5

    if day % 5 == 0:
        total_plunder = total_plunder * 0.7


#Print Ouput
if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = ( total_plunder / expected_plunder ) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")