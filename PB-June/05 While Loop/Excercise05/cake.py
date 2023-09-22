#user input
lenght_of_cake = int(input())
width_of_cake = int(input())
cake_pices = lenght_of_cake * width_of_cake
given_pieces = 0

#logic
while given_pieces < cake_pices:
    current_given_pieces = input()
    if current_given_pieces == "STOP":
        break
    given_pieces += int(current_given_pieces)

difference = abs(cake_pices - given_pieces)

#print output
if cake_pices >= given_pieces:
    print(f'{difference} pieces are left.')
else:
    print(f'No more cake left! You need {difference} pieces more.')
