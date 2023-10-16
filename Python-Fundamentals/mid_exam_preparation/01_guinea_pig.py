food_in_kg_to_grams = float(input()) * 1000
hay_in_kg_to_grams = float(input()) * 1000
cover_in_kg_to_grams = float(input()) * 1000
weight_in_kg_to_grams = float(input()) * 1000

for day in range(1, 31):
    if day % 2 == 0:
        food_in_kg_to_grams -= 300
        hay_in_kg_to_grams -= food_in_kg_to_grams * 0.05
    else:
        food_in_kg_to_grams -= 300
    if day % 3 == 0:
        cover_in_kg_to_grams -= weight_in_kg_to_grams * 0.333

    if food_in_kg_to_grams <= 0 or hay_in_kg_to_grams <= 0 or cover_in_kg_to_grams <= 0:
        break

if food_in_kg_to_grams <= 0 or hay_in_kg_to_grams <= 0 or cover_in_kg_to_grams <= 0:
    print('Merry must go to the pet store!')
else:
    print(f'Everything is fine! Puppy is happy! Food: {food_in_kg_to_grams/1000:.2f}, Hay: {hay_in_kg_to_grams/1000:.2f}, Cover: {cover_in_kg_to_grams/1000:.2f}.')

