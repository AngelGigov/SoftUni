import re

phone_numbers = input()

regex_impression = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

result = re.findall(regex_impression, phone_numbers)

print(', '.join(result))