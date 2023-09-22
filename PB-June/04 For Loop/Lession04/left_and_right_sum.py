#user input
digits = int(input())
left_number = 0
right_number = 0

#logic
for number in range(digits):
    number_left = int(input())
    left_number += number_left

for number in range(digits):
    number_right = int(input())
    right_number += number_right

if left_number == right_number:
    print(f'Yes, sum = {right_number}')
else:
    difference = abs(left_number - right_number)
    print(f'No, diff = {difference}')
