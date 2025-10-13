def check_happiness(happiness_list, factor):
    improved_happiness = [current_value * factor for current_value in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(num >= average_happiness for num in improved_happiness)
    total_count = len(improved_happiness)

    message = "happy" if happy_count >= total_count / 2 else "not happy"

    return f"Score: {happy_count}/{total_count}. Employees are {message}!"


employees_happiness = list(map(int, input().split(" ")))
factor = int(input())
result = check_happiness(employees_happiness, factor)
print(result)