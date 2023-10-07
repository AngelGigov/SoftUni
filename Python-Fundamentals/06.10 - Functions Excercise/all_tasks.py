# 1

def smallest(some_numbers: list):
    return min(some_numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
smallest_element = smallest([first_number, second_number, third_number])
print(smallest_element)


# 2
def sum_numbers(first, second):
    return first + second


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    returned_result = sum_numbers(first, second)
    final_result = subtract(returned_result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))


# 3

def all_the_characters(first_char: str, second_char: str) -> list:
    characters = []
    for current_character_as_digit in range(ord(first_char) + 1, ord(second_char)):
        characters.append(chr(current_character_as_digit))
    return characters


first_character = input()
second_character = input()
final_result = all_the_characters(first_character, second_character)
print(" ".join(final_result))


# 4


def odd_even_sums(some_number: str):
    sum_of_even = 0
    sum_of_odd = 0
    for digit in some_number:
        if int(digit) % 2 == 0:
            sum_of_even += int(digit)
        else:
            sum_of_odd += int(digit)
    return sum_of_odd, sum_of_even


number = input()
sum_of_odd_digits, sum_of_even_digits = odd_even_sums(number)
print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")

# 5

numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)


# 5.1
def is_even(number):
    return number % 2 == 0


numbers_as_string = input().split()
numbers_as_digits = []
for number in numbers_as_string:
    numbers_as_digits.append(int(number))
even_numbers = []
for element in numbers_as_digits:
    if is_even(element):  # if is_even(element) == True
        even_numbers.append(element)
print(even_numbers)

# 5.2

print([int(number) for number in input().split() if int(number) % 2 == 0])


# 8

def is_palindrome(some_number_as_string: str) -> bool:
    return some_number_as_string == some_number_as_string[::-1]


numbers_as_string = input().split(", ")
for number_as_string in numbers_as_string:
    print(is_palindrome(number_as_string))


# 9
def password_validator(some_password: str) -> list:
    list_of_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digits_counter = 0
    for character in some_password:
        if character.isdigit():
            digits_counter += 1
    if digits_counter < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
errors_in_password = password_validator(password)
if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))


# 10

def is_perfect(some_number: int) -> str:
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))


# 11

def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent = some_number // 10
    return f"{some_number}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number = int(input())
print(loading_bar(number))


# 12

def calculate_the_factorial(number):
    for current_number in range(1, number):
        number *= current_number
    return number  # initial number factorial -> number!


first_number = int(input())
second_number = int(input())
first_number_factorial = calculate_the_factorial(first_number)
second_number_factorial = calculate_the_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f"{result:.2f}")