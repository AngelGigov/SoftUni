def calculations(command: str, num_a: int, num_b: int):
    if command == 'multiply':
        return num_a * num_b
    elif command == 'divide':
        return int(num_a / num_b)
    elif command == 'add':
        return num_a + num_b
    elif command == 'subtract':
        return num_a - num_b

input_operator = input()
num_1 = int(input())
num_2 = int(input())

print(calculations(num_a=num_1, num_b=num_2, command=input_operator))