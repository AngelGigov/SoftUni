#User Input
starting_point = int(input())
end_point = int(input())

#Logic and print output
for char in range(starting_point, end_point + 1):
    print(chr(char), end=" ")