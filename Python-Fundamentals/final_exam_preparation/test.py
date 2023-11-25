string = "Hello"
number = int(input())

string = string[number:] + string[:number]

print(string)