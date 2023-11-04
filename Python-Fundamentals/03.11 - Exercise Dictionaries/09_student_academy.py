number_of_pairs = int(input())
students = {}

for i in range(number_of_pairs):
    name = input()
    grade = float(input())
    if name not in students:
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    average_grades = (sum(students[key]) / len(students[key]))
    if average_grades >= 4.50:
        print(f"{key} -> {average_grades:.2f}")