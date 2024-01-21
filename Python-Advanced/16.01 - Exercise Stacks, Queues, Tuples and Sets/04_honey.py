from collections import deque

honey = 0

bees = deque(int(el) for el in input().split())
nectar = [int(el) for el in input().split()]
symbol = deque(input().split())


functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}


while bees and nectar:

    curr_bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < curr_bee:
        bees.appendleft(curr_bee)
    else:
        honey += abs(functions[symbol.popleft()](curr_bee, curr_nectar))

print(f'Total honey made: {honey}')

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")