my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

start_index = 1
end_index = 4  # The end index is exclusive, so this will remove elements at indices 1, 2, and 3

del my_list[start_index:end_index]

print(my_list)
