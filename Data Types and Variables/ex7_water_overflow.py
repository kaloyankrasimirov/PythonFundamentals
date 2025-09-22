number_of_lines = int(input())
total_capacity = 255
current_capacity = 0

for current_line in range(number_of_lines):
    liters_of_water = int(input())

    if current_capacity + liters_of_water > total_capacity:
        print("Insufficient capacity!")
        continue
    else:
        current_capacity += liters_of_water
print(current_capacity)

