users = {}

command = input()
while command != "End":
    company, employee_id = command.split(" -> ")
    if company not in users:
        users[company] = []
    if employee_id not in users[company]:
        users[company].append(employee_id)
    command = input()

for key, values in users.items():
    print(key)
    for value in values:
        print(f"-- {value}")