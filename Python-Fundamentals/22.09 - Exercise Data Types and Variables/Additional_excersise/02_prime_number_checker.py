#User Input
number = int(input())
is_prime = False

if number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = True
            break

    # check if flag is True
print(is_prime)