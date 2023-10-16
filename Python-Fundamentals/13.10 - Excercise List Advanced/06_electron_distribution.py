def max_to_fill(index):
    max = 2 * index**2
    return max


number = int(input())
shell = []
current_index = 0

while number > 0:
    volume_to_fill = max_to_fill(current_index + 1)
    if volume_to_fill <= number:
        shell.append(volume_to_fill)
        number -= volume_to_fill
    else:
        shell.append(number)
        number = 0
    current_index += 1

print(shell)


