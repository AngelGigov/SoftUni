number_of_guests = int(input())

reservation_codes = set()

for _ in range(number_of_guests):
    command = input()
    reservation_codes.add(command)



command = input()
while command != "END":
    if command in reservation_codes:
        reservation_codes.remove(command)
    command = input()

print(len(reservation_codes))
if reservation_codes:
    for item in sorted(reservation_codes):
        print(item)