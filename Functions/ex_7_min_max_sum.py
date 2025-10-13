# def find_min(some_numbers: list) -> list:
#     return min(some_numbers)
#
# def find_max(some_numbers: list) -> list:
#     return max(some_numbers)
#
# def find_sum(some_numbers: list) -> int:
#     return sum(some_numbers)
#
# numbers_as_string = input().split()
# list_of_integers = []
# for current_number in numbers_as_string:
#         number = int(current_number)
#         list_of_integers.append(number)
#
# print(f"The minimum number is {find_min(list_of_integers)}")
# print(f"The maximum number is {find_max(list_of_integers)}")
# print(f"The sum number is: {find_sum(list_of_integers)}")


def calculate_stats(some_numbers: list) -> tuple:
    min_value = min(some_numbers)
    max_value = max(some_numbers)
    total_sum = sum(some_numbers)

    return min_value, max_value, total_sum

numbers_as_string = input().split()
list_of_integers = []
for current_number in numbers_as_string:
    number = int(current_number)
    list_of_integers.append(number)

min_res, max_res, total_res = calculate_stats(list_of_integers)

print(f"The minimum number is {min_res}")
print(f"The maximum number is {max_res}")
print(f"The sum number is: {total_res}")






