#User Input
command = input()
is_successfull = True

#Logic
while command != 'Welcome!':
    if command == "Voldemort":
        print("You must not speak of that name!")
        is_successfull = False
        break
    if len(command) < 5:
        print(f"{command} goes to Gryffindor.")
    elif len(command) == 5:
        print(f"{command} goes to Slytherin.")
    elif len(command) == 6:
        print(f"{command} goes to Ravenclaw.")
    elif len(command) > 6:
        print(f"{command} goes to Hufflepuff.")

    command = input()

if is_successfull:
    print("Welcome to Hogwarts.")