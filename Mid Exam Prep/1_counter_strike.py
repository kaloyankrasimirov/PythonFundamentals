# energy = int(input())
# won_battles = 0
#
#
# while True:
#     command = input()
#
#     if command == "End of battle":
#         print(f"Won battles: {won_battles}. Energy left: {energy}" )
#         break
#
#     distance = int(command)
#
#     if energy < distance:
#         print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
#         break
#
#
#     if energy >= distance:
#         won_battles += 1
#         energy -= distance
#         if won_battles % 3 == 0:
#             energy += won_battles



def counter_strike(energy:int) ->str:
    won_battles = 0
    while True:
        command = input()


        if command == "End of battle":
            return f"Won battles: {won_battles}. Energy left: {energy}"


        distance = int(command)

        if energy < distance:
            return f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy"


        if energy >= distance:
            won_battles += 1
            energy -= distance
            if won_battles % 3 == 0:
                energy += won_battles


initial_energy = int(input())
result = counter_strike(initial_energy)
print(result)