#user input

juniour_bicyclist = int(input())
senior_bicyclist = int(input())
trace_type = input()

sum_jun = 0
sum_sen = 0

#logic

if trace_type == 'trail':
    sum_jun = juniour_bicyclist * 5.5
    sum_sen = senior_bicyclist * 7
elif trace_type == 'cross-country':
    if juniour_bicyclist + senior_bicyclist > 50:
        sum_jun = juniour_bicyclist * (8 * 0.75)
        sum_sen = senior_bicyclist * (9.50 * 0.75)
    else:
        sum_jun = juniour_bicyclist * 8
        sum_sen = senior_bicyclist * 9.50
elif trace_type == 'downhill':
    sum_jun = juniour_bicyclist * 12.25
    sum_sen = senior_bicyclist * 13.75
elif trace_type == 'road':
    sum_jun = juniour_bicyclist * 20
    sum_sen = senior_bicyclist * 21.50

expenses = (sum_sen + sum_jun) * 0.05
total_sum = sum_jun + sum_sen - expenses

#print output
print(f'{total_sum:.2f}')