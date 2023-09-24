# 1

first_name = input()
second_name = input()
delimiter = input()
print(f"{first_name}{delimiter}{second_name}")

# 2

distance_in_meters = int(input())
distance_in_kilometers = distance_in_meters / 1000
print(f"{distance_in_kilometers:.2f}")

# 3

pounds = int(input())
usd = pounds * 1.31
print(f"{usd:.3f}")

# 4

centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} "
      f"years = {days} days = {hours} hours = {minutes} minutes")

# 5

number = int(input())
for current_number in range(1, number + 1):
    current_number_as_string = str(current_number)
    digits_sum = 0
    for digit in current_number_as_string:
        digits_sum += int(digit)
    is_special = False
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        is_special = True
    print(f"{current_number} -> {is_special}")

# 6.1

year = int(input())
year_is_special = False
while not year_is_special:
    year += 1
    year_as_string = str(year)
    year_is_special = True
    for digit in year_as_string:
        if year_as_string.count(digit) > 1:
            year_is_special = False
            break
print(year)

# 6.2

year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    repetition_counter = 1
    for index, digit in enumerate(year_as_string):
        for control_index in range(index + 1, len(year_as_string)):
            if year_as_string[control_index] == digit:
                repetition_counter += 1
                break
        if repetition_counter > 1:
            break
    if repetition_counter == 1:
        break
print(year)

# 6.3

year = int(input())
while True:
    year += 1
    year_as_string = str(year)
    if len(year_as_string) == len(set(year_as_string)):
        break
print(year)
