elements = input().split()
moves_count = 0
is_win = False

command = input()
while command != 'end':
    moves_count += 1
    first_index = int(command.split()[0])
    second_index = int(command.split()[1])

    if first_index == second_index or first_index < 0 or second_index < 0 or first_index > len(elements) or second_index > len(elements):
        elements.insert(int(len(elements) / 2), f"-{str(moves_count)}a")
        elements.insert(int(len(elements) / 2), f"-{str(moves_count)}a")
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        removed_element = elements.pop(first_index)
        elements.remove(removed_element)
    elif elements[first_index] != elements[second_index]:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves_count} turns!")
        is_win = True
        break

    command = input()


if is_win == False and len(elements) > 0:
    print("Sorry you lose :(")
    print(f"{' '.join(elements)}")


# elements = input().split()
# count_moves = 0
# command = input()
# while not command == "end":
#     count_moves += 1
#     first_element = int(command.split()[0])
#     second_element = int(command.split()[1])
#     if first_element == second_element or first_element < 0 or second_element < 0 or first_element >= len(elements) or second_element >= len(elements):
#         elements.insert(int(len(elements) / 2), f"-{str(count_moves)}a")
#         elements.insert(int(len(elements) / 2), f"-{str(count_moves)}a")
#         print("Invalid input! Adding additional elements to the board")
#     elif elements[first_element] == elements[second_element]:
#         print(f"Congrats! You have found matching elements - {elements[first_element]}!")
#         x = elements.pop(first_element)
#         elements.remove(x)
#     elif elements[first_element] != elements[second_element]:
#         print("Try again!")
#     if len(elements) == 0:
#         print(f"You have won in {count_moves} turns!")
#         break
#     command = input()
# if command == "end":
#     print("Sorry you lose :(\n"
#           f"{' '.join(elements)}")