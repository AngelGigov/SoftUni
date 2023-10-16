from math import ceil
#User input
number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
attendet_lectures = 0

for i in range(number_of_students):
    student_attendance = int(input())
    total_bonus = student_attendance / total_number_of_lectures * (5 + additional_bonus)
    if total_bonus >= max_bonus:
        max_bonus = total_bonus
        attendet_lectures = student_attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {attendet_lectures} lectures.")
