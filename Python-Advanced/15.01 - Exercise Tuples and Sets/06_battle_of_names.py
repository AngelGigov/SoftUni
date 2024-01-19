n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n + 1):
    name_to_numbers = sum(ord(el) for el in input()) // i

    if name_to_numbers % 2 == 0:
        even_set.add(name_to_numbers)
    else:
        odd_set.add(name_to_numbers)

sum_of_odd, sum_of_even = sum(odd_set), sum(even_set)

if sum_of_even == sum_of_odd:
    print(*odd_set.union(even_set), sep=', ')
elif sum_of_even < sum_of_odd:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')