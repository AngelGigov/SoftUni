from math import ceil

#user input
movie_name = input()
episode_lenght = int(input())
break_lenght = int(input())

lunch_time = break_lenght * 0.125
time_for_break = break_lenght * 0.25

remaining_time = break_lenght - time_for_break - lunch_time
#time_left = remaining_time - episode_lenght
time_left = ceil(abs(remaining_time - episode_lenght))

#logic
if remaining_time >= episode_lenght:
    print(f'You have enough time to watch {movie_name} and left with {time_left} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {movie_name}, you need {time_left} more minutes.')


#output
