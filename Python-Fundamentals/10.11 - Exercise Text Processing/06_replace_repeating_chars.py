text = input()
new_text = ''
last_character = ''

for current_character in text:
    if current_character != last_character:
        new_text += current_character
        last_character = current_character

print(new_text)