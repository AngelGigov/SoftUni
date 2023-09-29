#Read User Input
number_of_lines = int(input())
open_brackets = 0
closing_brackets = 0

#Logic
for i in range(number_of_lines):
    get_char = input()
    if get_char == '(':
        open_brackets += 1
    elif get_char == ')':
        closing_brackets += 1

#Print output
if open_brackets != closing_brackets:
    print('UNBALANCED')
else:
    print('BALANCED')



####### Another Solution from co's

lines = int(input())

is_balanced = True
last_bracket = ''
for _ in range(0, lines):
    current = input()
    if current not in ['(', ')']:
        continue

    if last_bracket == '' and current == ')' or last_bracket == current:
        is_balanced = False
        break

    last_bracket = current

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')