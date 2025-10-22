def calculations(numbers:list) -> int:
    average_score = 0
    for num in numbers:
        average_score += num / len(numbers)

    min_number = min(list_of_integers)
    max_number = max(list_of_integers)
    range_number = max_number - min_number
    final_list = []
    final_list.append(average_score)
    final_list.append(range_number)

    return final_list


list_of_integers = list(map(int, input().split()))
score = 0
result = calculations(list_of_integers)
print(result)


