from collections import deque

worms = [int(worm) for worm in input().split()]
holes = deque(int(hole) for hole in input().split())

all_worms_count = len(worms)
matches = 0

while worms and holes:
    current_hole = holes.popleft()

    if current_hole == worms[-1]:
        worms.pop()
        matches += 1
    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if matches:
    print(f'Matches: {matches}')
else:
    print("There are no matches.")

if not worms and matches == all_worms_count:
    print(f"Every worm found a suitable hole!")
elif not worms and matches < all_worms_count:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(el) for el in worms])}")

if not holes:
    print('Holes left: none')
else:
    print(f'Holes left: {", ".join(str(item) for item in holes)}')