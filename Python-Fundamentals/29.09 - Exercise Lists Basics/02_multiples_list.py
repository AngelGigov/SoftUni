#User input
factor_number = int(input())
count_number = int(input())

multiple_list = []

#Logic
for i in range(1, count_number + 1):
    multiple_list.append(i * factor_number)

#Print Output
print(multiple_list)