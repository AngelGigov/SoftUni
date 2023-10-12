array = input().split()
array = [int(i) for i in array] # making array
command = input().split()

while command[0] != 'end':
    if command[0] == 'swap':
        array[int(command[1])], array[int(command[2])] = array[int(command[2])], array[int(command[1])]
    elif command[0] == 'multiply':
        array[int(command[1])] = array[int(command[1])] * array[int(command[2])]
    elif command[0] == 'decrease':
        array = [i-1 for i in array]
    command = input().split()

array = [str(i) for i in array]
#print(array_to_numbers)
print(', '.join(array))

