import re

text = input()

destinations = []
travel_points = 0

pattern = r"([=|\/])([A-Z][A-Za-z]{2,})\1"

matches = re.findall(pattern, text)

if matches:
    for match in matches:
        destinations.append(match[1])
    travel_points = sum(len(destination) for destination in destinations)

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {travel_points}')


