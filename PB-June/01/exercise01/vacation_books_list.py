pages = int(input())
pages_per_hour = int(input())
days_for_book = int(input())

total_time_for_book = pages / pages_per_hour
needed_hours_per_day = total_time_for_book / days_for_book

print(int(needed_hours_per_day))