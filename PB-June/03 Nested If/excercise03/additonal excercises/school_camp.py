#user input
season = input()
group = input()
scholars = int(input())
nights_stay = int(input())

price = 0
sport_to_practice = ''
#logic

if group == 'boys':
    if season == "Winter":
        sport_to_practice = "Judo"
        price = scholars * nights_stay * 9.6
    elif season == "Spring":
        sport_to_practice = "Tennis"
        price = scholars * nights_stay * 7.2
    elif season == "Summer":
        sport_to_practice = "Football"
        price = scholars * nights_stay * 15
elif group == 'girls':
    if season == "Winter":
        sport_to_practice = "Gymnastics"
        price = scholars * nights_stay * 9.6
    elif season == "Spring":
        sport_to_practice = "Athletics"
        price = scholars * nights_stay * 7.2
    elif season == "Summer":
        sport_to_practice = "Voleyball"
        price = scholars * nights_stay * 15
elif group == 'mixed':
    if season == "Winter":
        sport_to_practice = "Ski"
        price = scholars * nights_stay * 10
    elif season == "Spring":
        sport_to_practice = "Cycling"
        price = scholars * nights_stay * 9.5
    elif season == "Summer":
        sport_to_practice = "Swimming"
        price = scholars * nights_stay * 20

#discount logic
if scholars >= 50:
    price *= 0.5
elif 20 <= scholars < 50:
    price *= 0.85
elif 10 <= scholars < 20:
    price *= 0.95

#print output
print(f'{sport_to_practice} {price:.2f} lv.')