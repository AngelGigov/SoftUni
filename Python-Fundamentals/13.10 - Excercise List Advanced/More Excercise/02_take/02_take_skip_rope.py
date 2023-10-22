read_string = input()
number_list = [int(x) for x in read_string if x.isnumeric()]
non_number_list = [x for x in read_string if not x.isnumeric()]
take_list = []
skip_list = []

for i in range(len(number_list)):
    if i % 2 == 0:
        take_list.append(number_list[i])
    else:
        skip_list.append(number_list[i])

result = ''

current_index = 0
for i in range(len(take_list)):
    result += ''.join(non_number_list[current_index:current_index + take_list[i]])
    current_index += take_list[i] + skip_list[i]

print(result)


