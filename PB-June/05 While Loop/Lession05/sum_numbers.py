#Input

num = int(input())

#logic
sum = 0

while True:
    user_input = int(input())
    sum += user_input
    if sum >= num:
        break


#output
print(sum)