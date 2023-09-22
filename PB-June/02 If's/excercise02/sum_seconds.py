#User Input

time_first_competitor = int(input())
time_second_competitor = int(input())
time_third_competitor = int(input())

#Logic


total_time_raw = time_first_competitor + time_second_competitor + time_third_competitor
total_time_minutes = total_time_raw // 60
total_time_seconds = total_time_raw % 60

#Output
if total_time_seconds < 10:
    print(f'{total_time_minutes}:0{total_time_seconds}')
else:
    print(f'{total_time_minutes}:{total_time_seconds}')
