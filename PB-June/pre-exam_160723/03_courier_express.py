# User Input
weight_of_parcel = float(input())
type = input()
distance = int(input())
cost_for_delivery = 0
additional_cost = 0

#Logic
if type == "standard":
    if weight_of_parcel < 1:
        cost_for_delivery = 0.03 * distance
    elif 1 <= weight_of_parcel < 10:
        cost_for_delivery = 0.05 * distance
    elif 10 <= weight_of_parcel < 40:
        cost_for_delivery = 0.10 * distance
    elif 40 <= weight_of_parcel < 90:
        cost_for_delivery = 0.15 * distance
    elif 90 <= weight_of_parcel < 150:
        cost_for_delivery = 0.2 * distance
elif type == "express":

    if weight_of_parcel < 1:
        additional_cost = 0.03 * 0.8 * weight_of_parcel * distance
        cost_for_delivery = (0.03 * distance) + additional_cost
    elif 1 <= weight_of_parcel < 10:
        additional_cost = 0.05 * 0.4 * weight_of_parcel * distance
        cost_for_delivery = (0.05 * distance) + additional_cost
    elif 10 <= weight_of_parcel < 40:
        additional_cost = 0.10 * 0.05 * weight_of_parcel * distance
        cost_for_delivery = (0.10 * distance) + additional_cost
    elif 40 <= weight_of_parcel < 90:
        additional_cost = 0.15 * 0.02 * weight_of_parcel * distance
        cost_for_delivery = (0.15 * distance) + additional_cost
    elif 90 <= weight_of_parcel < 150:
        additional_cost = 0.2 * 0.01 * weight_of_parcel * distance
        cost_for_delivery = (0.2 * distance) + additional_cost

#Print Output
print(f'The delivery of your shipment with weight of {weight_of_parcel:.3f} kg. would cost {cost_for_delivery:.2f} lv.')