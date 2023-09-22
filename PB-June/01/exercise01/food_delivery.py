#price of products
chicken_price = 10.35
fish_price = 12.40
vegeterian_price = 8.15

#take count of menues
chicken_menu_count = int(input())
fish_menu_count = int(input())
vegeterian_menu_count = int(input())

sum_chicken = chicken_menu_count * chicken_price
sum_fish = fish_menu_count * fish_price
sum_veggie = vegeterian_menu_count * vegeterian_price

total_sum = sum_fish + sum_chicken + sum_veggie

#additional charges
desert = total_sum * 0.2
delivery = 2.50

grand_total = total_sum + desert + delivery

print(round(grand_total, 2))
