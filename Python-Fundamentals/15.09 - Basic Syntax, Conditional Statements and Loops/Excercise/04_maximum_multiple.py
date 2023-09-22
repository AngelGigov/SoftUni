#User input
divisor = int(input())
boundary = int(input())

#Logic
for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        break
print(number)
