# User input
processor_price_in_usd = int(input())
processor_price_in_bgn = processor_price_in_usd * 1.57
video_card_price_in_usd = int(input())
video_card_price_in_bgn = video_card_price_in_usd * 1.57
ram_price_in_usd = int(input())
ram_price_in_bgn = ram_price_in_usd * 1.57
count_of_ram = int(input())
precentage_of_discount = float(input())

total_ram = count_of_ram * ram_price_in_bgn
processor_after_discount = processor_price_in_bgn * (1 - precentage_of_discount)
video_after_discount = video_card_price_in_bgn * (1 - precentage_of_discount)

total = total_ram + processor_after_discount + video_after_discount

# Print output
print(f'Money needed - {total:.2f} leva.')