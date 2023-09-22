#input
tabs_opened = int(input())
salary = float(input())

#logic
for current_tab in range(tabs_opened):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break

#printout
if salary > 0:
    print(int(salary))
else:
    print('You have lost your salary.')
