#User Input
movie_budget = float(input())
people_needed = int(input())
people_clothing_price = float(input())

#known expenses

movie_decor = movie_budget * 0.1

if people_needed > 150:
    people_clothing_price = people_clothing_price - (people_clothing_price * 0.1)
else:
    pass

clothes_total = people_needed * people_clothing_price

all_expenses = clothes_total + movie_decor

if all_expenses <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {abs(all_expenses - movie_budget):.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {abs(all_expenses - movie_budget):.2f} leva more.")