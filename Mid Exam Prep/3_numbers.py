my_numbers = list(map(int, input().split()))
average_value = sum(my_numbers) / len(my_numbers)
final_numbers = [number for number in my_numbers if number > average_value]

final_numbers.sort(reverse=True)

if not final_numbers:
    print("No")
else:
    print(*final_numbers[:5], sep=" ")