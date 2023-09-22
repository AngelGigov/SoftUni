#  Input
user_name = input()
password = input()

#logic
user_input = input()
while password != user_input:
    user_input = input()
    if user_input == password:
        break

print(f'Welcome {user_name}!')