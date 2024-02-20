def even_odd_filter(**kwargs):
    dictionary = {}
    for key, values in kwargs.items():
        if key == "even":
            dictionary[key] = [el for el in values if el % 2 == 0]
        elif key == 'odd':
            dictionary[key] = [el for el in values if el % 2 != 0]
    return dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
