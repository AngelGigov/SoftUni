#User Input

number_of_messages = int(input())

#Logic

for i in range(number_of_messages):
    code = int(input())
    if code == 88:
        print("Hello")
    elif code == 86:
        print("How are you?")
    elif code < 88:
        print('GREAT!')
    else: #elif code > 88:
        print('Bye.')