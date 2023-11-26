text = input()

command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        #if index < len(text)-1: #check if index is valid
        text = text[:index] + string + text[index:]
    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(text) and start_index <= end_index < len(text):
            text = text[:start_index] + text[end_index+1:]
    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        text = text.replace(old_string, new_string)
    print(text)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {text}")