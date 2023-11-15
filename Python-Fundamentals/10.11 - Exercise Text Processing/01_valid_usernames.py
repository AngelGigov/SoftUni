def lenght_is_valid(some_username):
    if 3 <= len(some_username) <= 16:
        return True
    return False

def characters_are_valid(some_username):
    for character in some_username:
        if not (character.isalnum() \
                or character == '_' \
                or character == '-'):
            return False
    return True

def no_redundant(some_username):
    if " " in some_username:
        return False
    return True

def username_is_valid(some_username):
    if lenght_is_valid(some_username) \
            and characters_are_valid(some_username) \
            and no_redundant(some_username):
        return True
    return False

usernames = input().split(', ')
for name in usernames:
    if username_is_valid(name):
        print(name)