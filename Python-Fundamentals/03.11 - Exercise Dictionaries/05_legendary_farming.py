key_materials = {"shards": 0, 'fragments': 0, 'motes': 0}
junk_materials = {}


while True:
    command = input().split()
    for item in range(0, len(command), 2):
        value = command[item]
        key = command[item + 1].lower()
        if key in key_materials:
            key_materials[key] += int(value)
        else:
            junk_materials[key] = int(value)
        if key_materials["shards"] >= 250 or key_materials["fragments"] >= 250 or key_materials["motes"] >= 250:
            print('obtained!')
            break



print(key_materials)
print(junk_materials)