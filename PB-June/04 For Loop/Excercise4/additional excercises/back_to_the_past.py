#input
money = float(input())
year_to_leave = int(input())

ivan_old = 18

#logic

for year in range(1800, year_to_leave + 1):
    if year % 2 == 0:
        money -= 12000
        ivan_old += 1
    elif year % 2 == 1:
        money -= 12000 + (50 * ivan_old)
        ivan_old += 1
    elif money < 0:
        break

if money >= 0:
    print(f'Yes! He will live a carefree life and will have {money:.2f} dollars left.')
else:
    print(f'He will need {abs(money):.2f} dollars to survive.')