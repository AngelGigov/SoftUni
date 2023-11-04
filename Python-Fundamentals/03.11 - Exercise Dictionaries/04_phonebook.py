phonebook = {}
number = 0

while True:
    command = input()
    if command.isdigit():
        number += int(command)
        break
    name, phone = command.split('-')
    phonebook[name] = phone

for i in range(number):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")

