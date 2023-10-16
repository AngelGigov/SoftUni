first_list = input().split(', ')
second_list = input().split(', ')

result = []

for substring in first_list:
    for word in second_list:
        if substring in word:
            result.append(substring)
            break

print(result)