inventory = input().split(", ")
while True:
    full_command = input().split()
    if full_command[0] == "Finish":
        break

    command = full_command[0]

    if command == "Remove":
        product_to_find = full_command[1]
        if product_to_find in inventory:
            inventory.remove(product_to_find)

    elif command == "Add":
        product_to_add = full_command[1]
        inventory.insert(0, product_to_add)

    elif command == "Swap":
        product1 = full_command[1]
        product2 = full_command[2]
        if product1 in inventory and product2 in inventory:
            index1 = inventory.index(product1)
            index2 = inventory.index(product2)
            inventory[index1], inventory[index2] = inventory[index2], inventory[index1]


print(" ".join(inventory))




