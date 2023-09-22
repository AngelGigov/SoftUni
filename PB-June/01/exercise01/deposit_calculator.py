
deposit_sum = float(input())
months = int(input())
yearly_interest_cercent = float(input())

interest = deposit_sum * yearly_interest_cercent / 100
per_month = interest / 12

result = deposit_sum + months * per_month

print(float(result))
