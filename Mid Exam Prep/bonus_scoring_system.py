from math import ceil
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for _ in range(number_of_students):

    attendance_of_each_student = int(input())
    bonus_per_student = attendance_of_each_student / number_of_lectures * (5 + additional_bonus)
    if bonus_per_student > max_bonus:
        max_bonus = bonus_per_student
        max_attendance = attendance_of_each_student


print(f"Max Bonus: {ceil(max_bonus)}.")
print(f'The student has attended {max_attendance} lectures.')