students_info = []
course_to_search = ''

while True:
    command = input()

    if ":" not in command:
        course_to_search = command
        break

    name, ID, course = command.split(":")
    students_info.append({'name': name, 'ID': ID, 'course': course})

for student in students_info:
    if course_to_search.startswith(student["course"][0:3]):
        print(f"{student['name']} - {student['ID']}")

