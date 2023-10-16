def possitive_numbers(list: list):
    positive_nums = [x for x in list if x >= 0]
    return positive_nums
def negative_numsbers(list: list):
    negative_num = [x for x in list if x < 0]
    return negative_num

def even_numbers(list):
    even_nums = [x for x in list if x % 2 == 0]
    return even_nums

def odd_numbers(list):
    odd_nums = [x for x in list if x % 2 != 0]
    return odd_nums

numbers = [int(num) for num in input().split(', ')]

positive = possitive_numbers(numbers)
negative = negative_numsbers(numbers)
even = even_numbers(numbers)
odd = odd_numbers(numbers)

print(f'Positive: {", ".join(map(str, positive))}')
print(f'Negative: {", ".join(map(str, negative))}')
print(f'Even: {", ".join(map(str, even))}')
print(f'Odd: {", ".join(map(str, odd))}')

