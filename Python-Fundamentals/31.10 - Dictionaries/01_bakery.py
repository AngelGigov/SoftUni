input_text = input().split()

food = {}

for i in range(0, len(input_text), 2):
    product = input_text[i]
    qty = input_text[i + 1]
    food[product] = int(qty)

print(food)

