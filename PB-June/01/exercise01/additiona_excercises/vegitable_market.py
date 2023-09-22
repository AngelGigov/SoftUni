price_per_kg_veg = float(input())
price_per_kg_frut = float(input())
sum_kg_veg = float(input())
sum_kg_frut = float(input())

total_price_veg = price_per_kg_veg * sum_kg_veg
total_price_frut = price_per_kg_frut * sum_kg_frut

grand_total_eur = (total_price_veg + total_price_frut) / 1.94

formated = "{:.2f}".format(grand_total_eur)

print(formated)
#print(grand_total_eur)
