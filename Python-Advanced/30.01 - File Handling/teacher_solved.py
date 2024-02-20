# ex_1
# import os
#
#
# ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
# file_name = "text.txt"
# path = os.path.join("..", "..", "nested_folder", file_name)
#
#
# try:
#     file = open("text.txt", "r")
#     print("File found")
# except FileNotFoundError:
#     print("File is not found")
#
# ex_2
# import os.path
#
# path = os.path.join("resources", "numbers.txt")
#
# file = open(path)
#
# total_amount = 0
# lines = file.readlines()
# file.close()
#
#
# for line in lines:
#     total_amount += int(line.strip())
#
# print(total_amount)
#
# ex_3
# with open("my_first_file.txt", "a") as file:
#     file.write("I just created my first file!")
#
# ex_4
# import os
#
# path = os.path.join("resources", "just_created.txt")
#
# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("File is already deleted")
#
#
# if os.path.exists(path):
#     os.remove(path)
# else:
#     print("File is already deleted")
#
# ex_5
# import os
# import re
#
# words_path = os.path.join("resources", "words.txt")
# text_path = os.path.join("resources", "input.txt")
# output_file_path = os.path.join("resources", "text.txt")
#
# with open(words_path) as file:
#     searched_words_as_text = file.read()
#     searched_words = [word.lower() for word in searched_words_as_text.split()]
#
# with open(text_path) as file:
#     content = file.read().lower()
#
#
# words_count = {}
#
# for searched_word in searched_words:
#     pattern = re.compile(rf"\b{searched_word}\b")
#     results = re.findall(pattern, content)
#     words_count[searched_word] = len(results)
#
# sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])
#
# with open(output_file_path, "a") as file:
#     for word, count in sorted_words_count:
#         file.write(f"{word} - {count}\n")
#
