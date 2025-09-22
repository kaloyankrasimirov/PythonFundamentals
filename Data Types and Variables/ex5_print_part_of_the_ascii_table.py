line_1 = int(input())
line_2 = int(input())

for index in range(line_1, line_2 + 1):
    if index == line_2:
        print(chr(index))
    else:
        print(chr(index), end=" ")