numbers = [int(num) for num in input().split()]
average_number = sum(numbers) / len(numbers)
top_numbers = [number for number in numbers if number > average_number]



if len(top_numbers) < 1:
    print('No')
else:
    x = sorted(top_numbers, key=lambda x: -x)
    print(*x[:5])








