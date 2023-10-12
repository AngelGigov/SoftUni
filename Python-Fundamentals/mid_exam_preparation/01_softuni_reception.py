first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
number_of_students = int(input())

students_handled_per_hour = first_employee + second_employee + third_employee
hour = 0

while 0 < number_of_students:
    hour += 1
    if hour % 4 == 0:
        continue
    number_of_students -= students_handled_per_hour

print(f'Time needed: {hour}h.')


