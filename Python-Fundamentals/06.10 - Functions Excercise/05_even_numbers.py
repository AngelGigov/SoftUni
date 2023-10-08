# numbers = list(map(int, input().split()))
#
# even = filter(lambda x: x % 2==0, numbers)
# print(list(even))

# print(list(filter(lambda x: x % 2==0, numbers)))


#################################
def even_numbers(list):
    even = []
    for digit in list:
        if int(digit) % 2 == 0:
            even.append(int(digit))
    return even

numbers = input().split()
evens = even_numbers(numbers)
print(evens)