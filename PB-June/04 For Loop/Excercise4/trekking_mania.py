#input
number_of_people = int(input())
musala = 0
mont_blanc = 0
kilimandjaro = 0
k2 = 0
everest = 0

#logic
for group in range(number_of_people):
    current_group = int(input())
    if current_group <= 5:
        musala += current_group
    elif current_group <= 12:
        mont_blanc += current_group
    elif current_group <= 25:
        kilimandjaro += current_group
    elif current_group <= 40:
        k2 += current_group
    elif current_group > 40:
        everest += current_group

total_count = musala + mont_blanc + kilimandjaro + k2 + everest

percentage_musala = musala / total_count * 100
percentage_mont_blanc = mont_blanc / total_count * 100
percentage_kilimandjaro = kilimandjaro / total_count * 100
percentage_k2 = k2 / total_count * 100
percentage_everest = everest / total_count * 100

print(f'{percentage_musala:.2f}%')
print(f'{percentage_mont_blanc:.2f}%')
print(f'{percentage_kilimandjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everest:.2f}%')
