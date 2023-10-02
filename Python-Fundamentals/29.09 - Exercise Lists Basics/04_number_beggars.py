#User input
money = input().split(', ')
beggers = int(input())
money = [int(x) for x in money]
final_sum = []
start_index = 0

#Logic
while start_index < beggers:
    current_begger_sum = 0
    for current_index in range(start_index, len(money), beggers):
        current_begger_sum += money[current_index]
    final_sum.append(current_begger_sum)
    start_index += 1

#Print Output
print(final_sum)






