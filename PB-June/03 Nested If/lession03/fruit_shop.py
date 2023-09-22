#user input
fruit = input()
day = input()
qty = float(input())

total = 0
is_valid = False

#Logic

if day== 'Monday' or day == "Tuesday" or day == 'Wednesday' or day == 'Thursday' or day == "Friday":
    if fruit == 'banana':
        total = qty * 2.50
        is_valid = True
    elif fruit == 'apple':
        total = qty * 1.20
        is_valid = True
    elif fruit == 'orange':
        total = qty * 0.85
        is_valid = True
    elif fruit == 'grapefruit':
        total = qty * 1.45
        is_valid = True
    elif fruit == 'kiwi':
        total = qty * 2.70
        is_valid = True
    elif fruit == 'pineapple':
        total = qty * 5.50
        is_valid = True
    elif fruit == 'grapes':
        total = qty * 3.85
        is_valid = True
elif day== 'Saturday' or day == "Sunday":
    if fruit == 'banana':
        total = qty * 2.70
        is_valid = True
    elif fruit == 'apple':
        total = qty * 1.25
        is_valid = True
    elif fruit == 'orange':
        total = qty * 0.90
        is_valid = True
    elif fruit == 'grapefruit':
        total = qty * 1.60
        is_valid = True
    elif fruit == 'kiwi':
        total = qty * 3
        is_valid = True
    elif fruit == 'pineapple':
        total = qty * 5.60
        is_valid = True
    elif fruit == 'grapes':
        total = qty * 4.20
        is_valid = True


#Print output
if is_valid == True:
    print(f'{total:.2f}')
else:
    print('error')



