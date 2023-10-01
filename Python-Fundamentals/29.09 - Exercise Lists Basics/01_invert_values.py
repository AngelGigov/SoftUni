#User input
input_numbers = list(map(int, input().split(' ')))
filtered_num = []

#Logic
for number in input_numbers:
    number *= -1
    filtered_num.append(number)


#Print Output
print(filtered_num)
