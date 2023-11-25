import re

text = input()
string_to_find = input()

pattern = fr'\b{string_to_find}\b'

match = re.findall(pattern, text, re.I)

print(len(match))

