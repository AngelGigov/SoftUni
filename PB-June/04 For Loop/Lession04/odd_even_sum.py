#user input
n = int(input())
odd_number = 0
even_number = 0

#logic
for number in range(1, n + 1):
    if number % 2 == 1:
        number_odd = int(input())
        odd_number += number_odd
    else:
        number_even = int(input())
        even_number += number_even

#print output
if odd_number == even_number:
    print('Yes')
    print(f'Sum = {even_number}')
else:
    difference = abs(odd_number - even_number)
    print('No')
    print(f'Diff = {difference}')