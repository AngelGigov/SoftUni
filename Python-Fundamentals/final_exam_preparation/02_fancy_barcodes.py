import re
pattern = r"@#+\b([A-Z][a-zA-Z0-9]{4,}[A-Z])\b@#+"

number_of_barcodes = int(input())

for line in range(number_of_barcodes):
    read_barcode = input()
    if re.match(pattern, read_barcode):
        num = re.findall(r'\d', read_barcode)
        if len(num) < 1:
            print(f'Product group: 00')
        else:
            print(f'Product group: {"".join(num)}')
    else:
        print('Invalid barcode')