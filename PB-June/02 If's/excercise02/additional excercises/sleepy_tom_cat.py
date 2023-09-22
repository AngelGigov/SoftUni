#user input
days_off = int(input())


#given infomation
toms_play_per_year = 30000

working_days = (365 - days_off)

real_time_for_play = (working_days * 63) + (days_off * 127)


norm_difference = abs(toms_play_per_year - real_time_for_play)

hours = norm_difference // 60
minutes = norm_difference % 60

if toms_play_per_year >= real_time_for_play:
    print('Tom sleeps well')
    print(f'{hours} hours and {minutes} minutes less for play')
else:
    print('Tom will run away')
    print(f'{hours} hours and {minutes} minutes more for play')