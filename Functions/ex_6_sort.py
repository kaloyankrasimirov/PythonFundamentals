def list_sorting(some_numbers: list) -> list:
    list_of_numbers = []
    for current_number in some_numbers:
        number = current_number
        list_of_numbers.append(number)

    return sorted(list_of_numbers)

numbers_as_string = input().split()
print(list_sorting(numbers_as_string))