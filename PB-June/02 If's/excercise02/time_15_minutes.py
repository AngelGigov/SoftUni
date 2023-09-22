#input
hours = int(input())
minutes = int(input())


#Logic
#we convert time to minuites and add the additonal minutes
time_in_minutes = hours * 60 + minutes + 15

final_hours = time_in_minutes // 60
final_minutes = time_in_minutes % 60

if final_hours >= 24:
    final_hours = final_hours // 24 - 1

if final_minutes < 10:
    print(f'{final_hours}:0{final_minutes}')
else:
    print(f'{final_hours}:{final_minutes}')