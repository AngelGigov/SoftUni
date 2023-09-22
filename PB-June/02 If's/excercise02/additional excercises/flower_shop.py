from math import ceil, floor

#User input

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())


#Price of the flowers
magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

#Totals per type_of_flower as per the order
magnolia_total = magnolia_price * magnolia_count
hyacinth_total = hyacinth_price * hyacinth_count
rose_total = rose_price * rose_count
cactus_total = cactus_price * cactus_count

total = magnolia_total + hyacinth_total + rose_total + cactus_total
vat = total * 0.05
total_vat =  total - vat

#user output
if total_vat >= gift_price:
    leftover = total_vat - gift_price
    print(f'She is left with {floor(leftover)} leva.')
else:
    needed_more = gift_price - total_vat
    print(f'She will have to borrow {ceil(needed_more)} leva.')

