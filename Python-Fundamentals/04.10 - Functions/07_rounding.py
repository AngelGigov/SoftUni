def rouding(list):
    intigers = []
    for obj in list:
        temp = round(float(obj))
        intigers.append(temp)
    return intigers

command = input().split()
print(rouding(command))
