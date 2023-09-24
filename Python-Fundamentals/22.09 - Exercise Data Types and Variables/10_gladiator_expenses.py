#User Input
lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0

#Logic
total_helmet_lost = lost_fights_count // 2
total_sword_lost = lost_fights_count // 3
total_shield_lost = lost_fights_count // (3 * 2)
total_armor_lost = total_shield_lost // 2

expenses = total_helmet_lost * helmet_price \
    + total_armor_lost * armor_price \
    + total_sword_lost * sword_price \
    + total_shield_lost * shield_price

#Print Output
print(f"Gladiator expenses: {expenses:.2f} aureus")
