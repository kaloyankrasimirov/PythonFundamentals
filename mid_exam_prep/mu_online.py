rooms = input().split("|")
health = 100
bitcoins = 0
best_run = 0
for room_index, room_content in enumerate(rooms):
    command_parts = room_content.split()

    action = command_parts[0]
    value = int(command_parts[1])

    if action == "potion":
        missing_health = 100 - health
        amount_to_heal = min(value, missing_health)
        if amount_to_heal > 0:
            health += amount_to_heal
            print(f"You healed for {amount_to_heal} hp.")
            print(f"Current health: {health} hp.")
        best_run += 1
    elif action == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")
        best_run += 1
    elif action != "potion" and action != "chest":
        health -= value
        if health > 0:
            print(f"You slayed {action}.")
            best_run += 1
        else:
            best_run += 1
            print(f"You died! Killed by {action}.")
            print(f"Best room: {best_run}")
            break

if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")



    # if action == "potion":
    #     if health == 100:
    #         best_run += 1
    #         continue
    #     else:
    #         healed_value = 100 - health
    #         health += value
    #         if health > 100:
    #             health = 100
    #             print(f"You healed for {healed_value} hp.")
    #             print(f"Current health: {health} hp.")
    #         elif health < 100:
    #             print(f"You healed for {value} hp.")
    #             print(f"Current health: {health} hp.")
    #         best_run += 1