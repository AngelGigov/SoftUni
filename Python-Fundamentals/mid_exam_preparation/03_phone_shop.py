phones_input = input().split(', ')

command = input()
while command != "End":
    action, phone = command.split(" - ")

    if action == "Add":
        if phone not in phones_input:
            phones_input.append(phone)
    elif action == "Remove":
        if phone in phones_input:
            phones_input.remove(phone)
    elif action == 'Bonus phone':
        old_phone, new_phone = phone.split(":")
        if old_phone in phones_input:
            index = phones_input.index(old_phone)
            phones_input.insert(index + 1, new_phone)
    elif action == 'Last':
        if phone in phones_input:
            index = phones_input.index(phone)
            remove = phones_input.pop(index)
            phones_input.append(remove)

    command = input()

print(', '.join(phones_input))