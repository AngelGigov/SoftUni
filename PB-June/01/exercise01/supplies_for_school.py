count_pens = int(input())
count_markers = int(input())
liters_of_alcohol = int(input())
percent_of_discount = int(input())

total_price_pens = count_pens * 5.80
total_price_markers = count_markers * 7.20
total_price_alcohol = liters_of_alcohol * 1.20

total_all_no_discount = total_price_pens + total_price_markers + total_price_alcohol
total_all_discount = total_all_no_discount - (total_all_no_discount * percent_of_discount / 100)

print(round(total_all_discount, 2))