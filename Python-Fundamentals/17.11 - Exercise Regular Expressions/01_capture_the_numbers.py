import re

line = input()

while line:
    regex = r'\d+'
    result = re.findall(regex, line)
    if result:
        print(" ".join(result), end= " ")
    line = input()