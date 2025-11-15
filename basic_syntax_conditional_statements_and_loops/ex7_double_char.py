while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    new_string = ""

    for char in command:
        new_string += char + char

    print(new_string)
