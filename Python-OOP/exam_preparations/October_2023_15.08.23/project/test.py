lst = [1, 2, 4, 5, 6, 7]

try:
    el = next(filter(lambda e: e == 3, lst))
except StopIteration:
    el = None


print(el)