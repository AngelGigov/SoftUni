#Read User Input
key = int(input())
number_of_lines = int(input())

#Lopic and Print Output
for i in range(number_of_lines):
    read_letter = ord(input())
    print(chr(read_letter + key), end='')
