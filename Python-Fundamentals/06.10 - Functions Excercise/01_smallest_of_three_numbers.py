def smallest_number_of_tree():
    smallest = []
    for i in range(3):
        number = int(input())
        smallest.append(number)
    return min(smallest)


print(smallest_number_of_tree())