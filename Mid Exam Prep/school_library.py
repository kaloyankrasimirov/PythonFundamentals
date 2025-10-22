book_list = input().split("&")

while True:
    command = input()
    command_parts = command.split(" | ")
    command_type = command_parts[0]

    if len(command_parts) > 1:
        book_name1 = command_parts[1]

    if command == "Done":
        print(", ".join(book_list))
        break
    if command_type == "Add Book":
        if book_name1 not in book_list:
            book_list.insert(0, book_name1)
    elif command_type == "Take Book":
        if book_name1 in book_list:
            book_list.remove(book_name1)
    elif command_type == "Swap Books":
        if len(command_parts) > 2:
            book_name2 = command_parts[2]
            if book_name1 in book_list and book_name2 in book_list:
                index_to_swap_1 = book_list.index(book_name1)
                index_to_swap_2 = book_list.index(book_name2)
                book_list[index_to_swap_1], book_list[index_to_swap_2] = book_list[index_to_swap_2], book_list[index_to_swap_1]
    elif command_type == "Insert Book":
        if book_name1 not in book_list:
            book_list.append(book_name1)
    elif command_type == "Check Book":
        if book_name1 and book_name1.isdigit():
            position = int(book_name1)
            index_to_check = position
            if 0 <= index_to_check < len(book_list):
                print(book_list[index_to_check])


