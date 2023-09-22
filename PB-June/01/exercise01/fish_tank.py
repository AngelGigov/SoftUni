lenght_cm = int(input())
widht_cm = int(input())
height_cm = int(input())
percent = float(input())

volume = lenght_cm * widht_cm * height_cm
volume_of_water = volume * 0.001
occupied_space = percent / 100

needed_water = volume_of_water * (1 - occupied_space)

print(needed_water)