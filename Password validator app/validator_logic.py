def check_length(some_password:str)-> bool:
    return 8 <= len(some_password) <= 64

def check_specials(some_password:str)-> bool:
    for symbol in some_password:
        specials_counter = 0
        if not symbol.isalnum():
            specials_counter += 1
        if specials_counter >= 1:
            return True

def check_digits(some_password:str)-> bool:
    digit_counter = 0
    for symbol in some_password:
        if symbol.isdigit():
            digit_counter += 1
        if digit_counter >= 1:
            return True

def check_upper_case(some_password: str)-> bool:
    upper_counter = 0
    for symbol in some_password:
        if symbol.isupper():
            upper_counter += 1
    if upper_counter >= 1:
        return True

def password_checker(some_password:str)-> None:
    if not check_length(some_password):
        print("The password must be at least 10 characters long.")
    if not check_specials(some_password):
        print("The password must contain at least one special character.")
    if not check_upper_case(some_password):
        print("The password must contain at least one letter, of which at least one must be uppercase.")
    if not check_digits(some_password):
        print("The password must contain at least one digit")

    if check_length(some_password) and\
            check_specials(some_password) and\
            check_digits(some_password) and\
            check_upper_case(some_password):
        print(f"Password is valid")

password = input()
password_checker(password)