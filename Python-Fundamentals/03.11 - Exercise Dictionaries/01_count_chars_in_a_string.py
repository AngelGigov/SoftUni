text_input = input()
char_count = {}
for char in text_input:
    if char == " ":
        continue
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for key, value in char_count.items():
    print(f"{key} -> {value}")