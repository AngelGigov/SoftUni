filepath = input().split('\\')
file = filepath[-1]
filename, extention = file.split('.')
print(f'File name: {filename}')
print(f'File extension: {extention}')

