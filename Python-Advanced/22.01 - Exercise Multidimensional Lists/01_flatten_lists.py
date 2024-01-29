line = input().split("|")

flatten_list = []

for el in line[::-1]:
    flatten_list.extend(el.split())

print(*flatten_list)