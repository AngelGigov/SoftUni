#input
name = input()
student_class = 1
fails = 0
avarage = 0

#logic
while True:
    grade_per_year = float(input())
    if grade_per_year < 4.00:
        fails += 1
        if fails > 1:
            print(f'{name} has been excluded at {student_class} grade')
            break
        continue
    student_class += 1
    avarage += grade_per_year
    if student_class > 12:
        print(f'{name} graduated. Average grade: {avarage/12:.2f}')
        break

