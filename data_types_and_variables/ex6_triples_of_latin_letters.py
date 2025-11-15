number = int(input())

for first_symbol in range(97, 97 + number):
    for second_symbol in range(97, 97 + number):
        for third_symbol in range(97, 97 + number):
            print(chr(first_symbol),chr(second_symbol),chr(third_symbol), sep="")
