# User input
serial_name = input()
seasons_count = int(input())
series_count = int(input())
duration_of_episode = float(input())


# Logic
adverts = duration_of_episode * 0.2
duration_of_episode += adverts
additional_time_for_season = seasons_count * 10
total_time = duration_of_episode * seasons_count * series_count + additional_time_for_season


# Print output
print(f'Total time needed to watch the {serial_name} series is {int(total_time)} minutes.')