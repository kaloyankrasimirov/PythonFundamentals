def check_length(password: str) -> str or bool:
    if 6 <= len(password) <= 10:
        return True
    return "Password must be between 6 and 10 characters"

def check_letters_and_digits(password: str) -> bool or str:
    if password.isalnum():
        return True
    return "Password must consist only of letters and digits"
def check_digits(password: str) -> bool or str:
    digits_counter = 0
    for symbol in password:
        if symbol.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    return "Password must have at least 2 digits"

def check_password(password: str) -> list:
    is_valid = []
    is_valid.append(check_length(password))
    is_valid.append(check_letters_and_digits(password))
    is_valid.append(check_digits(password))
    for index in range(len(is_valid) -1, -1, -1):
        if isinstance(is_valid[index], bool):
            is_valid.pop(index)
    return is_valid



input_password = input()
password_is_not_valid = check_password(input_password)
if password_is_not_valid:
    print('\n'.join(password_is_not_valid))
else:
    print("Password is valid")