from math import ceil

#user input
record_sec = float(input())
distance_meter = float(input())
time_sec = float(input())

resistance_in_sec = (distance_meter // 15) * 12.5


#Logic
time_of_ivan = distance_meter * time_sec + resistance_in_sec

#user output
if record_sec <= time_of_ivan:
    print(f'No, he failed! He was {time_of_ivan - record_sec:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {time_of_ivan:.2f} seconds.')
