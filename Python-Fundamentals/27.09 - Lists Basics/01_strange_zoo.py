#User input
strings = []

#Logic
for i in range(3):
    string = input()
    strings.append(string)

strings[0], strings[-1] = strings[-1], strings[0]

#Print output
print(strings)
