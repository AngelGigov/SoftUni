def sum_numbers(a, b):
    return a + b

def subtract(result, c):
    return result - c

def add_and_subtract(first_number, second_number, third_number):
    resultat = sum_numbers(first_number, second_number)
    final_result = subtract(resultat, third_number)
    return final_result

num_one = int(input())
num_two = int(input())
num_tree = int(input())

print(add_and_subtract(num_one, num_two, num_tree))