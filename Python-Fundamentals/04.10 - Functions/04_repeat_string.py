# def repeat_string(string, numbers_to_repeat):
#     return string * numbers_to_repeat
#
# user_input = input()
# num = int(input())
#
# print(repeat_string(user_input, num))

##########################################################################################

user_input = input()
num = int(input())

repeat_string = lambda a, b: a * b
print(repeat_string(user_input, num))