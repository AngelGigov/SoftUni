box_of_clotes = [int(x) for x in input().split()]
capacity = int(input())

rack_number = 1
left_capacity = capacity

while box_of_clotes:
    cloth = box_of_clotes.pop()
    if left_capacity >= cloth:
        left_capacity -= cloth
    else:
        rack_number += 1
        left_capacity = capacity
        left_capacity -= cloth
print(rack_number)