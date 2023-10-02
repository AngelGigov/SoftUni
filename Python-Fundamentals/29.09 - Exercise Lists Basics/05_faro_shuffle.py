#User Input
deck_of_cards = input().split()
number_of_shuffle = int(input())
middle = len(deck_of_cards) // 2
shuffled = []

#Logic
for i in range(number_of_shuffle):
    left_part = deck_of_cards[:middle]
    right_part = deck_of_cards[middle:]
    for shuffle in range(middle):
        shuffled.append(left_part[shuffle])
        shuffled.append(right_part[shuffle])

    deck_of_cards = shuffled.copy()
    shuffled.clear()

#Print Output
print(deck_of_cards)


