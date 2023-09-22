#user input
peter_budget = float(input())
videocard_count = int(input())
processor_count = int(input())
ram_memory_count = int(input())



#price of products
videocard_price = 250
processor_price = (videocard_price * videocard_count) * 0.35
ram_memory_price = (videocard_price * videocard_count) * 0.10

#totals
total_videocard = videocard_price * videocard_count
total_processor = processor_price * processor_count
total_ram = ram_memory_price * ram_memory_count

total_price = total_ram + total_processor + total_videocard

if videocard_count > processor_count:
    total_price = total_price - (total_price * 0.15)
else:
    pass

#user output
if peter_budget >= total_price:
    print(f'You have {peter_budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - peter_budget:.2f} leva more!')