# ex_1
# symbols = ("-", ",", ".", "!", "?")
#
# with open("files/file_1.txt", "r") as even_lines_file:
#     text = even_lines_file.readlines()
#
# for row in range(0, len(text), 2):
#
#     for symbol in symbols:
#         text[row] = text[row].replace(symbol, "@")
#
#     print(text[row][::-1])
#
# ex_2
# from string import punctuation
#
# with open("files/file_1.txt", "r") as text_file:
#     text = text_file.readlines()
#
# output_file = open("files/output_2.txt", "w")
#
# for row in range(len(text)):
#     letters, marks = 0, 0
#
#     for symbol in text[row]:
#         if symbol.isalpha():
#             letters += 1
#         elif symbol in punctuation:
#             marks += 1
#
#     output_file.write(f"Line {row + 1}: {text[row][:-1]} ({letters})({marks})\n")
#
# output_file.close()
#
# ex_3
# import os
#
# while True:
#     command, *info = input().split("-")  # Replace-text.txt-a-b -> [text.txt, a, b]
#
#     if command == "Create":
#         with open(f"files/{info[0]}", "w"): pass
#
#     elif command == "Add":
#         with open(f"files/{info[0]}", "a") as file:
#             file.write(f"{info[1]}\n")
#
#     elif command == "Replace":
#         try:
#             with open(f"files/{info[0]}", "r+") as file:
#                 text = file.read()
#                 text = text.replace(info[1], info[2])
#
#                 file.seek(0)
#                 file.write(text)
#                 file.truncate()
#
#         except FileNotFoundError:
#             print(f"An error occurred!")
#
#     elif command == "Delet":
#         try:
#             os.remove(f"files/{info[0]}")
#         except FileNotFoundError:
#             print(f"An error occurred!")
#
#     elif command == "End":
#         break
#
# ex_4
# import os
#
#
# def save_extensions(dir_name, first_level=False):
#     for filename in os.listdir(dir_name):
#         file = os.path.join(dir_name, filename)
#
#         if os.path.isfile(file):
#             extension = filename.split(".")[-1]
#             extensions[extension] = extensions.get(extension, []) + [filename]
#         elif os.path.isdir(file) and not first_level:
#             save_extensions(file, first_level=True)
#
#
# directory = input("Enter a directory: ")
# extensions = {}  # [py: [python.py, hello.py], ...}
# result = []
#
# try:
#     save_extensions(directory)
# except FileNotFoundError:
#     print("Directory not found!")
#
# extensions = sorted(extensions.items(), key=lambda x: x[0])
#
# for extension, files in extensions:  # extension => py, files => [one.py, two.py]...
#     result.append(f".{extension}")
#
#     for file in sorted(files):
#         result.append(f"- - - {file}")
#
# with open("files/report.txt", "w") as report_file:
#     report_file.write('\n'.join(result))
#
# ex_5
# import os
# import re
#
# directory = input("Enter a directory: ")
# string_to_replace = input("Enter a string to replace: ")
# string_to_replace_with = input("Enter a string to replace with: ")
#
# for filename in os.listdir(directory):
#     file = os.path.join(directory, filename)  # .\hello/file 1 => .\hello/file_1
#     # [., hello, file 1][:-1] => ./hello + "/" + new_name => ./hello/new_name
#     if os.path.isfile(file):
#         new_name = filename.replace(string_to_replace, string_to_replace_with)
#         new_file = "/".join(re.split(r"[\\/]", file)[:-1]) + "/" + new_name
#         os.rename(file, new_file)