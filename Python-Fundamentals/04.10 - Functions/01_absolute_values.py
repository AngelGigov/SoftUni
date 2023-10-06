#User Input
numbers = input().split()
output_list = []

#Logic
for number in numbers:
    output_list.append(abs(float(number)))

#Print Output
print(output_list)
