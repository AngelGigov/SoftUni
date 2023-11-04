items = {"shards": 0, "fragments": 0, "motes": 0}

value = 3
key = input()
if key not in items.keys():
    items[key] = 0
items[key] += value