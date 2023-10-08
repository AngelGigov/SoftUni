def sorting_numbers(numbers):
    num_as_int = []
    for num in numbers:
        num_as_int.append(int(num))
    return sorted(num_as_int)


input_from_user = input().split()
print(sorting_numbers(input_from_user))
