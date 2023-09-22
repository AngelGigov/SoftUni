min_number = int(input())

while True:
    user_input = input()
    if user_input == "Stop":
        break
    number = int(user_input)
    if number < min_number:
        min_number = number

print(min_number)