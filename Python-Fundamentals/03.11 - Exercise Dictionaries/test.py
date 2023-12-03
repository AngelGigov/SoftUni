text = input()
companies = {}

while text != 'End':
    text_spl = text.split(' -> ')
    company = text_spl[0]
    employee = text_spl[1]
    if company not in companies:
        companies[company] = []
    if employee not in companies[company]:
        companies[company].append(employee)

    text = input()

for key, employee in companies:
    print(key)
    for name in employee:
        print(f'-- {name}')