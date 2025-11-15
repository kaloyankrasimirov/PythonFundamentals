def rounding_number(some_numbers: list) -> list:
    list_of_numbers = []
    for current_number in some_numbers:
        number = round(float(current_number))
        list_of_numbers.append(number)

    return list_of_numbers


numbers_as_string = input().split()
print(rounding_number(numbers_as_string))