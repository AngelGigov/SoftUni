#user input

type = input()
output = 'unknown'

#logic
if type == 'banana' or type == 'apple' or type == 'kiwi' or type == 'cherry' or type == 'lemon' or type == 'grapes':
    output = 'fruit'
elif type == 'tomato' or type == 'cucumber' or type == 'pepper' or type == 'carrot':
    output = 'vegetable'

#print output
print(output)