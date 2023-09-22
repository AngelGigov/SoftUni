#User Input
command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    else:
        for i in range(len(command)):
            print(command[i]+command[i], end='')
    print()
    command = input()