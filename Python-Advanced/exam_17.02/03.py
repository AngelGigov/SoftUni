def cookbook(*args):
    cook = {}

    for arg in args:
        recipe, country, ingredient = arg
        if country not in cook:
            cook[country] = []
        cook[country].append((recipe, ingredient))

    sorted_list = sorted(cook.keys(), key=lambda x: (-len(cook[x]), x))

    text = ''
    for key in sorted_list:
        text += f'{key} cuisine contains {len(cook[key])} recipes:\n'
        recipes = sorted(cook[key], key=lambda x: x[0])
        for recipe in recipes:
            text += f'  * {recipe[0]} -> Ingredients: {", ".join(recipe[1])}\n'

    return text

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
