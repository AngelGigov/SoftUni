def grocery_store(**kwargs):
    text = ''
    sorted_products = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    for product, qty in sorted_products:
        text += f'{product}: {qty}\n'

    return text



print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
