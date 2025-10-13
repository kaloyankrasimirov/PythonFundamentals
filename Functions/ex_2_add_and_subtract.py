def sum_numbers(first: int, second: int) -> int:
    return first + second

def subtract(some_result: int, thrid:int) -> int:
    return some_result - thrid

def add_and_subtract(first_integer: int, second_integer: int, third_integer: int) -> int:
    returned_result = sum_numbers(first_integer, second_integer)
    final_result = subtract(returned_result, third_integer)
    return final_result

num1 = int(input())
num2 = int(input())
num3 = int(input())
result = add_and_subtract(num1, num2, num3)
print(result)