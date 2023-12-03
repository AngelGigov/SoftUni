import re

text = input()
regex = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"
emojies = re.findall(regex, text)

#Counting the threshold
take_numbers = re.findall(f'\d', text)
threshold = 1
for i in take_numbers:
    threshold *= int(i)


print(f'Cool threshold: {threshold}')
print(f'{len(emojies)} emojis found in the text. The cool ones are:')

#Print Emoji if emoji score is > threshold
score = 0
for emoji in emojies:
    for el in emoji[1]:
        score += ord(el)
    if score > threshold:
        print(''.join(emoji))
    score = 0




