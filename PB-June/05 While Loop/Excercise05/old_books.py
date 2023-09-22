#  User Input
favorite_book = input()
book_checked = 0
is_found = False
#  Logic
current_book = input()

while current_book != "No More Books":
    if current_book == favorite_book:
        is_found = True
        break
    book_checked += 1
    current_book = input()

#  Print output
if is_found:
    print(f'You checked {book_checked} books and found it.')
else:
    print("The book you search is not here!")
    print(f"You checked {book_checked} books.")
