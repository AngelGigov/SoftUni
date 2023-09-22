#user input
day_time = int(input())
week_day = input()



#logic

if not week_day == "Sunday" and 10 <= day_time <= 18:
    print('open')
else:
    print('closed')

#print output


