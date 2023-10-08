def characters_in_range(start, stop):
    for i in range(ord(start) + 1, ord(stop)):
        print(chr(i), end=' ')


input_a = input()
input_b = input()
characters_in_range(input_a, input_b)