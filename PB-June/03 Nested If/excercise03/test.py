# 8
hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())
time_of_exam = hour_of_exam * 60 + minutes_of_exam
time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving

if time_of_arriving > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print("On time")
elif time_of_exam - 30 > time_of_arriving:  # else
    print("Early")
difference = abs(time_of_exam - time_of_arriving)
hours = difference // 60
minutes = difference % 60
if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f"{minutes} minutes before the start")
elif time_of_arriving <= time_of_exam - 60:
    print(f"{hours}:{minutes:02d} hours before the start")
elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f"{minutes} minutes after the start")
elif time_of_arriving >= time_of_exam + 60:
    print(f"{hours}:{minutes:02d} hours after the start")

# 9

day = int(input())
type_of_room = input()
rating = input()
nights = day - 1
prise_per_night = 0
if type_of_room == "room for one person":
    prise_per_night = 18
elif type_of_room == "apartment":
    prise_per_night = 25
    if nights < 10:
        prise_per_night *= 0.7
    elif nights <= 15:
        prise_per_night *= 0.65
    elif nights > 15:  # else
        prise_per_night *= 0.5
elif type_of_room == "president apartment":  # else
    prise_per_night = 35
    if nights < 10:
        prise_per_night *= 0.9
    elif nights <= 15:
        prise_per_night *= 0.85
    elif nights > 15:  # else
        prise_per_night *= 0.8
total_sum = nights * prise_per_night
if rating == "positive":
    total_sum *= 1.25
elif rating == "negative":  # else
    total_sum *= 0.9
print(f"{total_sum:.2f}")