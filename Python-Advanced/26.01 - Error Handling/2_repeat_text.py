text = input()

try:
    times = int(input())
    print(f'{text * times}')
except ValueError:
    print("Variable times must be an integer")