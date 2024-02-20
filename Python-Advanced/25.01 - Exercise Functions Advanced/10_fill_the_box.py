from collections import deque

def fill_the_box(height, lenght, width, *args):
    cubes_size = int(height) * int(lenght) * int(width)

    left_cubes = deque(args[:-1])

    for i in args:
        if i == "Finish":
            break
        if cubes_size - int(i) < 0:
            return f"No more free space! You have {sum(left_cubes)} more cubes."
        else:
            cubes_size -= int(i)
            left_cubes.popleft()
    return f"There is free space in the box. You could put {cubes_size} more cubes."








print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
