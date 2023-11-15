# 1

def length_is_valid(some_username):
    if 3 <= len(some_username) <= 16:
        return True
    return False


def characters_are_valid(some_username):
    for character in some_username:
        if not (character.isalnum() \
                or character == "-" \
                or character == "_"):
            return False
    return True


def no_redundant_symbols(some_username):
    if " " in some_username:
        return False
    return True


def username_is_valid(some_username):
    if length_is_valid(some_username) \
            and characters_are_valid(some_username) \
            and no_redundant_symbols(some_username):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)

# 2


first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    # Multiplication
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total_sum += ord(first_string[index])
elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total_sum += ord(second_string[index])
elif len(second_string) == len(first_string):  # else
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
print(total_sum)

# 3

filepath = input().split("\\")
filename_and_extension = filepath[-1]
filename, extension = filename_and_extension.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")

# 4

message = input()
encrypted_message = ""
for character in message:
    encrypted_character = chr(ord(character) + 3)
    encrypted_message += encrypted_character
print(encrypted_message)

# 5

single_string = input()
for index in range(len(single_string)):
    if single_string[index] == ":":
        print(f":{single_string[index + 1]}")

# 6

text = input()
final_message = ""
last_added_character = ""
for current_character in text:
    if current_character != last_added_character:
        final_message += current_character
        last_added_character = current_character
print(final_message)

# 7

some_string = input()
final_string = ""
strength = 0
for index in range(len(some_string)):
    # We have explostion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    # We have explosion mark
    elif some_string[index] == ">":
        final_string += some_string[index]
        strength += int(some_string[index + 1])
    # We have no explosion -> normal character
    else:
        final_string += some_string[index]
print(final_string)

# 9


text = input()
rage_message = ""
repetitions = ""
current_symbol = ""
for index in range(len(text)):
    if not text[index].isdigit():  # We have non-numeric character
        current_symbol += text[index].upper()
    else:  # We have digit here --> time for repetition
        for next_symbols in range(index, len(text)):
            if not text[next_symbols].isdigit():
                break
            repetitions += text[next_symbols]
        rage_message += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)


# 10

def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbol_repetition = match_symbol * uninterrupted_match_length
            # We have winning ticket
            if winning_symbol_repetition in left_part \
                    and winning_symbol_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for current_ticket in tickets:
    print(check_ticket(current_ticket))