import re

string = input()
paired_word = []
pattern = r"([@|#])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"

matches = re.findall(pattern, string)
count_of_words = len(matches)

for pair in matches:
    if pair[1] == pair[3][::-1]:
        paired_word.append(f'{pair[1]} <=> {pair[3]}')

if count_of_words > 0:
    print(f"{count_of_words} word pairs found!")
    if not paired_word:
        print('No mirror words!')
    else:
        print('The mirror words are:')
        print(', '.join(paired_word))
else:
    print('No word pairs found!')
    print('No mirror words!')