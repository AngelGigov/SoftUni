#user input
town = input()
volume = float(input())

commission = 0
is_valid = False

#logic
if 0 <= volume <= 500:
    if town == 'Sofia':
        commission = volume * 0.05
        is_valid = True
    elif town == 'Varna':
        commission = volume * 0.045
        is_valid = True
    elif town == 'Plovdiv':
        commission = volume * 0.055
        is_valid = True
elif 500 < volume <= 1000:
    if town == 'Sofia':
        commission = volume * 0.07
        is_valid = True
    elif town == 'Varna':
        commission = volume * 0.075
        is_valid = True
    elif town == 'Plovdiv':
        commission = volume * 0.08
        is_valid = True
elif 1000 < volume <= 10000:
    if town == 'Sofia':
        commission = volume * 0.08
        is_valid = True
    elif town == 'Varna':
        commission = volume * 0.10
        is_valid = True
    elif town == 'Plovdiv':
        commission = volume * 0.12
        is_valid = True
elif volume > 10000:
    if town == 'Sofia':
        commission = volume * 0.12
        is_valid = True
    elif town == 'Varna':
        commission = volume * 0.13
        is_valid = True
    elif town == 'Plovdiv':
        commission = volume * 0.145
        is_valid = True

#user output

if is_valid == True:
    print(f'{commission:.2f}')
else:
    print('error')
