# User input
eggs_size = input()
colour_of_eggs = input()
count_of_partides = int(input())

total_price = 0

# Logic
if eggs_size == "Large":
    if colour_of_eggs == "Red":
        total_price = count_of_partides * 16
    elif colour_of_eggs == "Green":
        total_price = count_of_partides * 12
    elif colour_of_eggs == "Yellow":
        total_price = count_of_partides * 9
elif eggs_size == "Medium":
    if colour_of_eggs == "Red":
        total_price = count_of_partides * 13
    elif colour_of_eggs == "Green":
        total_price = count_of_partides * 9
    elif colour_of_eggs == "Yellow":
        total_price = count_of_partides * 7
elif eggs_size == "Small":
    if colour_of_eggs == "Red":
        total_price = count_of_partides * 9
    elif colour_of_eggs == "Green":
        total_price = count_of_partides * 8
    elif colour_of_eggs == "Yellow":
        total_price = count_of_partides * 5


total_price *= 0.65

# Print Output
print(f'{total_price:.2f} leva.')
