# ex_1
#
# def calc_sum(nums, idx=0):
#     if idx == len(nums) - 1:
#         return nums[idx]
#
#     return nums[idx] + calc_sum(nums, idx + 1)
#
#
# nums = [int(x) for x in input().split()]
# print(calc_sum(nums))
#
# ex_2
#
# def get_factorial(n: int):
#     if n == 0:
#         return 1
#
#     return n * get_factorial(n - 1)
#
#
# n = int(input())
# print(get_factorial(n))
#
# ex_3
#
# def recursive_drawing(n):
#     if n == 0:
#         return
#
#     print('*' * n)
#
#     recursive_drawing(n - 1)
#
#     print('#' * n)
#
#
# n = int(input())  # 2
# recursive_drawing(n)
#
# ex_4
#
# def choose_coins(coins, target):
#     coins.sort(reverse=True)
#     idx = 0
#     used_coins = {}  # coin: times_used
#
#     while target > 0 and idx < len(coins):
#         count_current_coins = target // coins[idx]  # 4,50 => 1 * 4
#         target = target % coins[idx]  # 4,50 % 1 => 0.50
#
#         if count_current_coins > 0:
#             used_coins[coins[idx]] = count_current_coins
#
#         idx += 1
#
#     if target != 0:
#         return "Error"
#     else:
#         result = f"Number of coins to take: {sum(used_coins.values())}\n"
#
#         for coin, count in used_coins.items():
#             result += f"{count} coin(s) with value {coin}\n"
#
#         return result
#
#
# coins = [int(x) for x in input().split(", ")]
# target = int(input())
# print(choose_coins(coins, target))
#
# ex_5
# def set_cover(universe, sets):
#     chosen_sets = []
#
#     while universe:
#         best_set = max(sets, key=lambda s: len(universe.intersection(s)))
#         chosen_sets.append(best_set)
#         universe -= best_set
#
#     return chosen_sets
#
#
# universe = {int(x) for x in input().split(", ")}
# num_sets = int(input())
# sets = [{int(x) for x in input().split(", ")} for _ in range(num_sets)]
#
# result = set_cover(universe, sets)
#
# for i in range(len(result)):
#     result[i] = sorted(result[i])
#
# print(f"Sets to take ({len(result)}):")
# [print("{ " + f"{', '.join(str(x) for x in s)}" + " }") for s in result]
#
# ex_6
# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1
#
#     while left <= right:
#         mid_idx = (left + right) // 2
#         mid_el = numbers[mid_idx]
#
#         if mid_el == target:
#             return mid_idx
#         elif mid_el < target:
#             left = mid_idx + 1
#         elif mid_el > target:
#             right = mid_idx - 1
#
#     return -1
#
#
# nums = [int(x) for x in input().split()]
# target = int(input())
#
# print(binary_search(nums, target))
#
# ex_7
# def selection_sort(nums):
#     for idx in range(len(nums)):
#         min_idx = idx  # 0
#
#         for curr_idx in range(idx + 1, len(nums)):
#             if nums[curr_idx] < nums[min_idx]:
#                 min_idx = curr_idx
#
#         nums[idx], nums[min_idx] = nums[min_idx], nums[idx]
#
#
# nums = [int(x) for x in input().split()]
# selection_sort(nums)
# print(*nums)
#
# ex_8
#
# def bubble_sort(nums):
#     is_sorted = False
#     i = 0
#
#     while not is_sorted:
#         is_sorted = True
#
#         for j in range(1, len(nums) - i):
#             if nums[j - 1] > nums[j]:
#                 nums[j], nums[j - 1] = nums[j - 1], nums[j]
#                 is_sorted = False
#
#         i += 1
#
#
# nums = [int(x) for x in input().split()]
# bubble_sort(nums)
# print(*nums)
#
# ex_9
# def insertion_sort(nums):
#     for i in range(1, len(nums)):  # започваме от 1, защото на 0 е сортираната част
#         key = nums[i]  # взимаме key, защото при разместването, ще се загуби
#         j = i - 1  # взимаме последната стойност на сортираната част
#
#         # докато не стигнем началото
#         # и докато не стигнем позиция, на която да поставим ключа
#         while j >= 0 and nums[j] > key:
#             nums[j + 1] = nums[j]  # shift-ваме елемента
#             j -= 1  # местим се наляво
#
#         nums[j + 1] = key  # слагаме ключа на валидната позиция
#
#
# nums = [int(x) for x in input().split()]
# insertion_sort(nums)
# print(*nums)