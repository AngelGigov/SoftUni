#user input
kilometers = int(input())
day_time = input()

price = 0



#Logic
if kilometers < 20:
    if day_time == "day":
        price = kilometers * 0.79 + 0.70
    elif day_time == "night":
        price = kilometers * 0.90 + 0.70
elif kilometers > 100:
    price = kilometers * 0.06
else:
    price = kilometers * 0.09

#output
print(f'{price:.2f}')