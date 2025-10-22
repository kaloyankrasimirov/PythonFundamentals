initial_array = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == "end":
        print(*initial_array, sep=", ")
        break

    if command[0] == "swap":
        element_1 = int(command[1])
        element_2 = int(command[2])
        initial_array[element_1], initial_array[element_2] = initial_array[element_2], initial_array[element_1]


    elif command[0] == "multiply":
        element_1 = int(command[1])
        element_2 = int(command[2])
        initial_array[element_1] = initial_array[element_1] * initial_array[element_2]

    elif command[0] == "decrease":
        for num in range(len(initial_array)):
            initial_array[num] -= 1


# def swap(array:str, index1:int, index2:int ) -> None:
#     array[index1], array[index2] = array[index2], array[index1]
#
# def multiply(array:str, index1:int, index2:int) -> None:
#     array[index1] = array[index1] * array[index2]
#
# def decrease(array:str) -> None:
#     for num in range(len(array)):
#         array[num] -= 1
# #
#
# def resolution():
#     initial_array = list(map(int, input().split()))
#
#     while True:
#         command = input().split()
#
#         if command[0] == "end":
#             print(*initial_array, sep=", ")
#
#         if command[0] == "swap":
#             index1 = int(command[1])
#             index2 = int(command[2])
#             swap(initial_array, index1, index2)
#
#         elif command[0] == "multiply":
#             index1 = int(command[1])
#             index2 = int(command[2])
#             multiply(initial_array, index1, index2)
#
#         elif command[0] == "decrease":
#             decrease(initial_array)
#
# resolution()