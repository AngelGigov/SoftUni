courses_information = {}

command = input()
while command != 'end':
    course, name = command.split(' : ')
    if course not in courses_information:
        courses_information[course] = []
    courses_information[course].append(name)

    command = input()

for course, names in courses_information.items():
    print(f"{course}: {len(names)}")
    for name in names:
        print(f"-- {name}")