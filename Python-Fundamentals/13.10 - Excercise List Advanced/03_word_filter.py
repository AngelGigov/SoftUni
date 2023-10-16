def only_even_words(list):
    even_words_list = [word for word in list if len(word) % 2 == 0]
    return even_words_list


words = input().split()
print('\n'.join(only_even_words(words)))

