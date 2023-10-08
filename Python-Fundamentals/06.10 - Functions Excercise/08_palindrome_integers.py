def palindrome(number):
    return number == number[::-1]

user_input = input().split(', ')
for user_input in user_input:
    print(palindrome(user_input))