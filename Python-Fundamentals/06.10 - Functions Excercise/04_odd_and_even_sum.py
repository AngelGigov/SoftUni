def sumation_of_even_and_odd(number):
    sum_odd = []
    sum_even = []
    for i, num in enumerate(number):
        if int(num) % 2 == 0:
            sum_even.append(int(num))
        else:
            sum_odd.append(int(num))
    print(f'Odd sum = {sum(sum_odd)}, Even sum = {sum(sum_even)}')


intiger = input()
sumation_of_even_and_odd(intiger)