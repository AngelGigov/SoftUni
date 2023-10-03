# 1
list_with_numbers = input().split()
opposite_numbers = []
for number in list_with_numbers:
    current_number = -int(number)
    opposite_numbers.append(current_number)
print(opposite_numbers)

# 1.1

print([-int(number) for number in input().split()])

# 2
factor = int(input())
count = int(input())
list_with_numbers = []
for multiplier in range(1, count + 1):
    list_with_numbers.append(factor * multiplier)
print(list_with_numbers)

# 3

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
players = input().split()
game_was_terminated = False
for player in players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:  # if game_was_terminated == True
    print("Game was terminated")

# 4
money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integers = []
for current_money in money_as_string:
    money_as_integers.append(int(current_money))
final_sums = []
start_index = 0
while start_index < number_of_beggars:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integers), number_of_beggars):
        current_beggar_sum += money_as_integers[current_index]
    final_sums.append(current_beggar_sum)
    start_index += 1
print(final_sums)

# 5
deck_of_cards = input().split()
count_of_shuffles = int(input())
for shuffle in range(count_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_deck]
    right_part = deck_of_cards[middle_of_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_part)):  # (len(right_part))
        deck_after_shuffling.append(left_part[card_index])
        deck_after_shuffling.append(right_part[card_index])
    deck_of_cards = deck_after_shuffling
print(deck_after_shuffling)

#7
gifts = input().split(' ')

command = input().split(' ')
while command[0] != 'No' and command[1] != 'Money':
    index = 0
    if command[0] == 'OutOfStock':
        gift = command[1]
        gifts = list(map(lambda lst: lst.replace(gift, "None"), gifts))

    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gifts):
            gifts[index] = command[1]

    elif command[0] == 'JustInCase':
        gifts[-1] = command[1]

    command = input().split(' ')

while 'None' in gifts:
    gifts.remove('None')

for i in gifts:
    print(i, end=' ')


# 10
events = input().split("|")
total_coins = 100
total_energy = 100
factory_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    # type_of_event, event_value = event.split("-")
    # event_value = int(event_value)
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            factory_is_open = False
            break
if factory_is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:  # factory_is_open = False
    print(f"Closed! Cannot afford {type_of_event}.")
