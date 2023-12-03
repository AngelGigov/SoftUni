import re

regex = r"!([A-Z][a-z]{2,})!:\[([A-Za-z]+)\]"

number = int(input())


for i in range(number):
    text_input = input()
    match = re.match(regex, text_input)
    if match:
        command = match.group(1)
        string = match.group(2)
        letters_to_numbers = [str(ord(i)) for i in string]
        print(f"{command}: {' '.join(letters_to_numbers)}")
    else:
        print('The message is invalid')
