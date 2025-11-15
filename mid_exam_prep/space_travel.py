travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for rout_index, rout_content in enumerate(travel_route):
    command_parts = rout_content.split()
    action = command_parts[0]
    if action == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    value = int(command_parts[1])
    if action == "Travel":
        distance_travelled = value
        fuel_consumed = fuel - distance_travelled
        if fuel >= distance_travelled:
            print(f"The spaceship travelled {distance_travelled} light-years.")
            fuel -= distance_travelled
        else:
            print("Mission failed.")
            break
    if action == "Enemy":
        enemy_armor = value
        if ammunition >= enemy_armor:
            ammunition -= enemy_armor
            print(f"An enemy with {enemy_armor} armour is defeated.")
        elif ammunition < enemy_armor:
            fuel_to_escape = enemy_armor * 2
            if fuel_to_escape <= fuel:
                fuel -= fuel_to_escape
                print(f"An enemy with {enemy_armor} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif action == "Repair":
        fuel += value
        ammunition += value * 2
        print(f"Ammunitions added: {(value *2)}.")
        print(f"Fuel added: {value}.")