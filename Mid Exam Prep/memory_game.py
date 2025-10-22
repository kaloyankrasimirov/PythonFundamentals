string_to_remember = input().split()
number_of_turns = 0

while True:
    command = input()
    if command == "end":
        if string_to_remember:
            print("Sorry you lose :(")
            print(*string_to_remember, sep=" ")
            break
        else:
            print(f"You have won in {number_of_turns} turns!")
            break

    current_attempt = list(map(int, command.split()))
    index_1 = current_attempt[0]
    index_2 = current_attempt[1]
    sequence_length = len(string_to_remember)

    if index_1 == index_2 or index_1 < 0 or index_1 >= sequence_length or \
        index_2 < 0 or index_2 >= sequence_length:
        number_of_turns += 1
        string_to_remember.insert((len(string_to_remember) // 2), f"-{number_of_turns}a")
        string_to_remember.insert((len(string_to_remember) // 2), f"-{number_of_turns}a")
        print("Invalid input! Adding additional elements to the board")

    elif string_to_remember[index_1] == string_to_remember[index_2]:
        number_of_turns += 1
        found_element = string_to_remember[index_1]
        if index_1 > index_2:
            string_to_remember.pop(index_1)
            string_to_remember.pop(index_2)
        else:
            string_to_remember.pop(index_2)
            string_to_remember.pop(index_1)

        print(f"Congrats! You have found matching elements - {found_element}!")

        if not string_to_remember:
            print(f"You have won in {number_of_turns} turns!")
            break
    else:
        number_of_turns += 1
        print("Try again!")

