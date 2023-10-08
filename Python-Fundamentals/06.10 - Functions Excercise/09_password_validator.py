def password_validator(password):
    list_of_errors = []
    if len(password) < 6 or len(password) > 10:
        list_of_errors.append('Password must be between 6 and 10 characters')
    if not password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digits = 0
    for i in password:
        if i.isdigit():
            digits += 1
    if digits < 2:
        list_of_errors.append('Password must have at least 2 digits')

    return list_of_errors

password = input()
errors_in_password = password_validator(password)
if not errors_in_password:
    print("Password is valid")
else:
    print("\n".join(errors_in_password))

