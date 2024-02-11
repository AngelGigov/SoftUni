def recursive_power(num, power):
    total = 1
    if power == 0:
        return total
    total = num * recursive_power(num, power - 1)
    return total

print(recursive_power(2, 10))