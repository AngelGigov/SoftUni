#User Input
age = int(input())

#Logic
if age <= 14: # kids
    print('drink toddy')
elif age <= 18:   # teen
    print('drink coke')
elif age <= 21:   # young adaut
    print('drink beer')
else:            # adaut
    print('drink whisky')