#user input
exam_hour = int(input())
exam_minutes = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

#logic
exam_time_min = exam_hour * 60 + exam_minutes
arrival_time_min = hour_of_arrival * 60 + minutes_of_arrival

if exam_time_min - 30 <= arrival_time_min:
    print("Late")
elif exam_time_min == arrival_time_min:
    print('On time')
elif exam_time_min >= arrival_time_min:
    print('Early')