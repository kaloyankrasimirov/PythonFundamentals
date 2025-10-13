def rectangle_area_calculator(some_width: int, some_height: int) -> int:
    return some_width * some_height


width = int(input())
height = int(input())
result = rectangle_area_calculator(width, height)
print(result)