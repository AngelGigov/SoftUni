string_one, string_two = input().split()
total = 0

if len(string_one) > len(string_two):
    for character in range(len(string_two)):
        total += ord(string_one[character]) * ord(string_two[character])
    for character in range(len(string_two), len(string_one)):
        total += ord(string_one[character])
elif len(string_one) < len(string_two):
    for character in range(len(string_one)):
        total += ord(string_one[character]) * ord(string_two[character])
    for character in range(len(string_one), len(string_two)):
        total += ord(string_two[character])
elif len(string_one) == len(string_two): #Else
    for character in range(len(string_one)):
        total += ord(string_one[character]) * ord(string_two[character])


print(total)