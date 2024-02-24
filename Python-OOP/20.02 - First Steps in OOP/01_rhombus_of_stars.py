n = int(input())

def print_row(size, row):
    print(" " * (size - row), "* " * row)

def create_top_rhombus_part(size):
    for row in range(1, size + 1):
        print_row(size, row)

def create_bottom_rhombus_part(size):
    for row in range(size - 1, 0, -1):
        print_row(size, row)


def print_rhombus(size):
    create_top_rhombus_part(size)
    create_bottom_rhombus_part(size)

print_rhombus(n)


