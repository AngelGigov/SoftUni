# 1

import re

line = input()
while line:
    pattern = "\d+"
    matches = re.findall(pattern, line)
    if matches:
        print(" ".join(matches), end=" ")
    line = input()

# 2
import re

sentence = input()
pattern = r"\b_([A-Za-z0-9]+)\b"
variables = re.findall(pattern, sentence)
print(",".join(variables))

# 3
import re

sentence = input()
searched_word = input()
pattern = fr"(?i)\b{searched_word}\b"
matches = re.findall(pattern, sentence)
print(len(matches))

# 4

import re

sentence = input()
pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
extracted_emails = re.findall(pattern, sentence)
for extracted_email in extracted_emails:
    print(extracted_email[0])

# 5

import re

bought_furniture = []
total_cost = 0
pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")

# 6


import re

pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
line = input()
while line:
    match = re.search(pattern, line)
    if match:
        valid_url = match.group(1)
        print(valid_url)
    line = input()