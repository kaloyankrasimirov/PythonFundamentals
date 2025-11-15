numbers_as_a_string = input().split(" ")
count_of_numbers_to_remove = int(input())
numbers_as_int = []

for numbers in numbers_as_a_string:
    numbers_as_int.append(int(numbers))

elements_to_remove = numbers_as_int.copy()
elements_to_remove.sort()
elements_to_remove = elements_to_remove[:count_of_numbers_to_remove]
for element in elements_to_remove:
    numbers_as_int.remove(element)

#the 2nd block can be also presented as:
# elements_to_remove = sorted(numbers_as_int)[:count_of_numbers_to_remove]
# for element in elements_to_remove:
#     numbers_as_int.remove(element)

final_list_as_string = []
for number in numbers_as_int:
    final_list_as_string.append(str(number))

result = ", ".join(final_list_as_string)

print(result)
