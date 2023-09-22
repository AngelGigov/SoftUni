# User Input
number_of_students = int(input())

top_students = 0
between_four_and_five = 0
between_tree_and_four = 0
failed = 0
sum_of_grades = 0



# Logic
for student in range(number_of_students):
    score_of_exam = float(input())
    sum_of_grades += score_of_exam
    if score_of_exam < 3.00:
        failed += 1
    elif score_of_exam <= 3.99:
        between_tree_and_four += 1
    elif score_of_exam <= 4.99:
        between_four_and_five += 1
    elif score_of_exam >= 5.00:
        top_students += 1

avarage = sum_of_grades / number_of_students
percent_top_students = top_students / number_of_students * 100
percent_between_four_and_five = between_four_and_five / number_of_students * 100
percent_between_tree_and_four = between_tree_and_four / number_of_students * 100
percent_failed = failed / number_of_students * 100

# Print Output

print(f'Top students: {percent_top_students:.2f}%')
print(f'Between 4.00 and 4.99: {percent_between_four_and_five:.2f}%')
print(f'Between 3.00 and 3.99: {percent_between_tree_and_four:.2f}%')
print(f'Fail: {percent_failed:.2f}%')
print(f'Average: {avarage:.2f}')