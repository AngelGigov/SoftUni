text = input()
digit = ''
letters = ''
other = ''

for letter in text:
    if letter.isdigit():
        digit += letter
    elif letter.isalpha():
        letters += letter
    else:
        other += letter

print(digit)
print(letters)
print(other)