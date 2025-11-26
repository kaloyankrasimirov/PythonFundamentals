cities = {}
while True:
    command = input()
    if command == "Sail":
        command = input()
        command = command.split("=>")
        event = command[0]
        # if event == "Plunder":
        #     cities = plunder(cities, command)
        # elif event == "Prosper":
        #     cities = prosper(cities, command)
        print(event)
    else:
        command = command.split("||")
        city, population, gold = command[0], int(command[1]), int(command[2])
        if city not in cities:
            cities[city] = {'population': population, 'total_gold': gold}
        else:
            cities[city]['population'] += population
            cities[city]['total_gold'] += gold
        print(city, population, gold)
    break
