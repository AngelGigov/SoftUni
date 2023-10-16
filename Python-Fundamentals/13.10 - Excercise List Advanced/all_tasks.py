# 1

first_sequence = input().split(", ")
second_sequence = input().split(", ")
substrings = []
for first_string in first_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            substrings.append(first_string)
            break
print(substrings)

# 1.1
first_sequence = input().split(", ")
second_sequence = input().split(", ")
print([first_string for first_string in first_sequence if
       any(first_string in second_string for second_string in second_sequence)])

# 2

version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print(".".join(str(number) for number in version))

# 3

words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words))


# 4

def positive_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) >= 0])


def negative_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) < 0])


def even_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 == 0])


def odd_numbers(list_of_numbers):
    return ', '.join([number for number in list_of_numbers if int(number) % 2 != 0])


numbers = input().split(", ")
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")


# 5

def check_the_rooms(number_of_rooms):
    free_chairs = 0
    for number_of_room in range(1, number_of_rooms + 1):
        free_chairs_in_current_room, visitors = input().split()
        difference = len(free_chairs_in_current_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        free_chairs += difference
    return free_chairs


count_of_rooms = int(input())
total_free_chairs = check_the_rooms(count_of_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

# 6

number_of_electrons = int(input())
shells = []
for shell in range(1, number_of_electrons + 1):
    max_electrons_in_current_shell = 2 * shell ** 2
    if number_of_electrons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
        number_of_electrons -= max_electrons_in_current_shell
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break
print(shells)

# 7


numbers = [int(number) for number in input().split(", ")]
current_group = 10
while numbers:
    filtered_numbers_for_current_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_numbers_for_current_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_numbers_for_current_group]

# 9
text = input().split()
command = input().split()
while command[0] != "3:1":
    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
        if end_index > len(text) - 1:
            end_index = len(text) - 1
        merged_elements = "".join(text[start_index:end_index + 1])
        # text = text[0:start_index] + [merged_elements] + text[end_index +1]
        text[start_index:end_index + 1] = [merged_elements]
    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        element = text[index]
        divided_partition = []
        partition_length = len(element) // partitions
        for current_element_index in range(partitions):
            if current_element_index != partitions - 1:
                divided_partition.append(
                    element[current_element_index * partition_length: (current_element_index + 1) * partition_length])
            else:
                divided_partition.append(element[current_element_index * partition_length:])
        text[index:index + 1] = divided_partition

    command = input().split()
print(" ".join(text))

