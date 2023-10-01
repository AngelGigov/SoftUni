#User Input
num = int(input())
secret_word = input()
strings = []
filtered_strings = []

#Logic
for i in range(num):
    word = input()
    strings.append(word)
    if secret_word in word:
        filtered_strings.append(word)

#Output
print(strings)
print(filtered_strings)

