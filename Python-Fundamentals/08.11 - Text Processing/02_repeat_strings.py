input_str = input().split()
new_text = [txt * len(txt) for txt in input_str]
print(''.join(new_text))