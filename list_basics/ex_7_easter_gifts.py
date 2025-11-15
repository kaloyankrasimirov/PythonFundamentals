gifts_to_buy = input().split()

while True:
    full_command = input().split()
    if full_command[0] == "No" and full_command[1] == "Money":
        break

    command = full_command[0]

    if command == "OutOfStock":
        gift_to_find = full_command[1]
        for i in range(len(gifts_to_buy)):
            if gifts_to_buy[i] == gift_to_find:
                gifts_to_buy[i] = "None"
    elif command == "Required":
        item = full_command[1]
        index_number = int(full_command[2])
        if 0 <= index_number < len(gifts_to_buy):
            gifts_to_buy[index_number] = item
    elif command == "JustInCase":
        new_gift = full_command[1]
        new_gift = gifts_to_buy[-1]

final_gifts = []
for item in gifts_to_buy:
    if item != "None":
        final_gifts.append(item)

print(" ".join(final_gifts))