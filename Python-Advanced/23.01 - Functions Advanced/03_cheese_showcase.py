def sorting_cheeses(**kwargs):
    result = ''
    sorted_items = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for cheese, quantity in sorted_items:
        result += cheese + '\n'
        for qty in sorted(quantity, reverse=True):
            result += f"{qty}\n"

    return result






print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)

