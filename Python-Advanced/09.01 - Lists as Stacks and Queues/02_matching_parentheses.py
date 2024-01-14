string = input()

stack = []

for index in range(len(string)):
    if string[index] == "(":
        stack.append(index)
    elif string[index] == ")":
        start_index = stack.pop()
        end_index = index + 1
        print(string[start_index:end_index])

