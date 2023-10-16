journal = input().split(', ')

command = input()
while command != 'Craft!':
    action, item = command.split(' - ')
    if action == 'Collect':
        if item in journal:
            command = input()
            continue
        else:
            journal.append(item)
    elif action == 'Drop':
        if item in journal:
            journal.remove(item)
        else:
            command = input()
            continue
    elif action == 'Combine Items':
        old_item, new_item = item.split(':')
        if old_item in journal:
            index_of_item = journal.index(old_item)
            journal.insert((index_of_item + 1), new_item)
        else:
            command = input()
            continue
    elif action == 'Renew':
        if item in journal:
            journal.remove(item)
            journal.append(item)
        else:
            command = input()
            continue

    command = input()
print(', '.join(journal))
