#  Input
parcel = int(input())
price = 0
microbus = 0
truck = 0
train = 0

#  Logic
for i in range(parcel):
    tonage = int(input())
    if tonage <= 3:
        microbus += tonage
        price += 200 * tonage
    elif tonage <= 11:
        truck += tonage
        price += 175 * tonage
    elif tonage >= 12:
        train += tonage
        price += 120 * tonage

count_of_tonnage = microbus + truck + train
average_price = price / count_of_tonnage # need to find avarage

microbus_percentage = microbus / count_of_tonnage * 100
truck_percentage = truck / count_of_tonnage * 100
train_percentage = train / count_of_tonnage * 100


#  Output
print(f'{average_price:.2f}')
print(f'{microbus_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')
