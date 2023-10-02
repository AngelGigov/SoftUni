#User Input
list_of_integer = list(map(int, input().split(' '))) #You are taking str, so convert it to int
count_of_numbers_to_remove = int(input())

#Logic
for number in range(count_of_numbers_to_remove):
    smallest = min(list_of_integer)
    list_of_integer.remove(smallest)

#Print Outpu
print(', '.join(map(str, list_of_integer))) #Converting it back to str and removign "[ ]"