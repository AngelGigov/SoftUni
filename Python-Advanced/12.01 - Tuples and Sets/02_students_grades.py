n = int(input())

name_grade = {}

for _ in range(n):
    name, grade_as_str = tuple(input().split())
    value = float(grade_as_str)

    if name not in name_grade:
        name_grade[name] = []
    name_grade[name].append(value)

for key, value in name_grade.items():
    average_score = sum(value) / len(value)
    formated_grades = f"{' '.join([f'{g:.2f}' for g in value])}"
    print(f'{key} -> {formated_grades} (avg: {average_score:.2f})')
