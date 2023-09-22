# User input
kozunak_count = int(input())
baker_score = 0
best_score = 0
best_baker_name = ''

# Logic
for i in range(kozunak_count):
    baker_name = input()
    baker_score = 0
    while True:
        user_input = input()
        if user_input == "Stop":
            print(f'{baker_name} has {baker_score} points.')
            if baker_score > best_score:
                print(f'{baker_name} is the new number 1!')
                best_score = baker_score
                best_baker_name = baker_name
            break
        points = int(user_input)
        baker_score += points

# Print output
print(f'{best_baker_name} won competition with {best_score} points!')