def min_max_sum(numbers: list):
    input_as_int = []
    for i in numbers:
        input_as_int.append(int(i))
    return min(input_as_int), max(input_as_int), sum(input_as_int)



numbers = input().split()
min, max, sum = min_max_sum(numbers)

print(f'The minimum number is {min}')
print(f'The maximum number is {max}')
print(f'The sum number is: {sum}')