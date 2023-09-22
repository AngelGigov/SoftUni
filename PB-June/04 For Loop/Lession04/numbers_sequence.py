#read user input
n = int(input())


#logic
min_value = int(input())
max_value = min_value

for i in range(n - 1):
    num = int(input())
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num
#output
print(f'Max number: {max_value}')
print(f'Min number: {min_value}')