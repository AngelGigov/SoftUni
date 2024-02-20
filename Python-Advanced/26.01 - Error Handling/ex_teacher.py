
#ex_1

# numbers_list = [int(el) for el in input().split(", ")]
# result = 1
#
# for i in range(len(numbers_list)):
#     number = numbers_list[i]
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(result)

#ex_2
#
# text = input()
#
# try:
#     times = int(input())
#     print(text*times)
# except ValueError:
#     print("Variable times must be an integer")

#ex_3

# class ValueCannotBeNegative(Exception):
#     pass
#
# for _ in range(5):
#     number = int(input())
#
#     if number < 0:
#         raise ValueCannotBeNegative