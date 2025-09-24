number = int(input())

my_list = []
my_new_list = []

for _ in range(number):
    current_number = int(input())
    my_list.append(current_number)

command = input()


if command == "even":
    for numbers in my_list:
        if numbers % 2 == 0:
            my_new_list.append(numbers)
elif command == "odd":
    for numbers in my_list:
        if numbers % 2 != 0:
            my_new_list.append(numbers)
elif command == "negative":
    for numbers in my_list:
        if numbers < 0:
            my_new_list.append(numbers)
elif command == "positive":
    for numbers in my_list:
       if numbers >= 0:
            my_new_list.append(numbers)


print(my_new_list)

