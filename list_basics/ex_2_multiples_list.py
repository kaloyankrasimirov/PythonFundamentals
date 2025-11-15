factor = int(input())
count = int(input())

list = []

for number in range(1, count +1):
    current_number = number * factor
    list.append(current_number)
print(list)
