def is_even(number:int) -> bool:
    return number % 2 == 0

numbers_as_string = input().split()
result = []
for current_number in numbers_as_string:
    if is_even(int(current_number)):
        result.append(int(current_number))
print(result)