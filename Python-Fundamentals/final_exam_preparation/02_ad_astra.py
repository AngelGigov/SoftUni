import re

text = input()

pattern = r"(?i)([#|])([a-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)(\1)"

matches = re.findall(pattern, text, re.I)

total_callories = sum([int(match[3]) for match in matches])

print(f'You have food to last you for: {total_callories // 2000} days!')

for i in matches:
    product = i[1]
    exp_date = i[2]
    callories = i[3]
    print(f'Item: {product}, Best before: {exp_date}, Nutrition: {callories}')

