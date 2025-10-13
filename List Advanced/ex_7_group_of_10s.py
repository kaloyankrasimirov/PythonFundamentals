numbers = [int(number) for number in input().split(", ")]
group = 10
while numbers: #while len(numbers) > 0
    list_of_current_group_numbers = [number for number in numbers if number <= group]
    print(f"Group of {group}'s: {list_of_current_group_numbers}")
    numbers = [number for number in numbers if number not in list_of_current_group_numbers]
    group += 10

