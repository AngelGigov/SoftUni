numbers_as_string = input().split(', ')
numbers_as_intigers = [index for index, x in enumerate(numbers_as_string) if int(x) % 2 == 0]

print(numbers_as_intigers)