nailon_per_meter = int(input())
paint_in_liters = int(input())
paint_thinner = int(input())
hours_working = int(input())

all_nailon = nailon_per_meter + 2
all_paint = paint_in_liters + (paint_in_liters * 0.1)

sum_nailon = all_nailon * 1.50
sum_paint = all_paint * 14.50
sum_thinner = paint_thinner * 5.00
bags = 0.40

all_materials = sum_nailon + sum_paint + sum_thinner + bags
workers = (all_materials * 0.3) * hours_working

total = all_materials + workers

print(total)




