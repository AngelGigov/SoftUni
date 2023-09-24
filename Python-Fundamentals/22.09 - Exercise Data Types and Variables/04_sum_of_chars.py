#User input
number_of_char = int(input())
total_sum = 0

#Logic
for char in range(number_of_char):
    character = input()
    total_sum += ord(character)

#Print Output
print(f"The sum equals: {total_sum}")
