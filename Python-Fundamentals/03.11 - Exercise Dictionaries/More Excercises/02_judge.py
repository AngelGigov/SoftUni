data = {}
command = input()
while command != 'no more time':
    username, contest, points = command.split(" -> ")
    if username not in data:
        data[username] = {contest: points}
    else: #{'Peter': {"OOP": 400}} [username][contest]
        if contest in data[username]:
            if data[username][contest] < points:
                data[username][contest] = points
            else:
                pass
        else:
            data[username][contest] = points


    command = input()
print(data)