from collections import deque

pump_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pump_data.copy()
gas_in_tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pump_data.rotate(-1)
        pumps_data_copy = pump_data.copy()
        index += 1
        gas_in_tank = 0

print(index)
