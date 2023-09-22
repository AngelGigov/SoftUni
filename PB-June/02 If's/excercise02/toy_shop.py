#Toy prices
puzzle_price = 2.60
talking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
toy_truck_price = 2

#User input
excursion_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
toy_truck_count = int(input())

#Logic

#calculate revenue
revenue_puzzle = puzzle_price * puzzle_count
revenue_talking_doll = talking_doll_price * talking_doll_count
revenue_teddybear = teddy_bear_price * teddy_bear_count
revenue_minion = minion_price * minion_count
revenue_toy_tryck = toy_truck_price * toy_truck_count

#total revenue
total_revenue = revenue_puzzle + revenue_talking_doll + revenue_teddybear + revenue_minion + revenue_toy_tryck

all_toys_count = puzzle_count + talking_doll_count + teddy_bear_count + minion_count + toy_truck_count

if all_toys_count >= 50:
    total_revenue = total_revenue - (total_revenue * 0.25)

profit = total_revenue - (total_revenue * 0.1)



#Ouput
if profit >= excursion_price:
    print(f'Yes! {profit - excursion_price:.2f} lv left.')
else:
    print(f'Not enough money! {abs(profit - excursion_price):.2f} lv needed.')