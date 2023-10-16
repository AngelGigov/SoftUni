word = input().split()
searched_palindrome = input()
palindromes = [x for x in word if x == x[::-1]]
print(palindromes)
print(f'Found palindrome {palindromes.count(searched_palindrome)} times')


