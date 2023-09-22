#  User Input
max_bad_grade = int(input())
avarage_grade = 0
bad_grades_counter = 0
total_problems_solved = 0
last_problem_soved = ''
is_failed = False

current_problem = input()
#  Logic
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == max_bad_grade:
            is_failed = True
            break
    avarage_grade += current_grade
    total_problems_solved += 1
    last_problem_soved = current_problem
    current_problem = input()


#  Print Output
if is_failed:
    print(f'You need a break, {bad_grades_counter} poor grades.')
else:
    avarage_grade /= total_problems_solved
    print(f'Average score: {avarage_grade:.2f}')
    print(f'Number of problems: {total_problems_solved}')
    print(f'Last problem: {last_problem_soved}')