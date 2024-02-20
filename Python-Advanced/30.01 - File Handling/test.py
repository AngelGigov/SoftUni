import os



file_name = 'text.txt'

#path = os.path.join('directory', file_name)

try:
    file = open(file_name) #(path)
    print("File Found")
except FileNotFoundError:
    print("File is not found")