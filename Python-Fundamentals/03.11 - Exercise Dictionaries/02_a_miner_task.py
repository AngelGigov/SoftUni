resources = {}

counter = 0

while True:
    command = input()
    if command == "stop":
        break

    key = command
    value = int(input())
    if key not in resources:
        resources[key] = value
    else:
        resources[key] += value

for key, value in resources.items():
    print(f"{key} -> {value}")