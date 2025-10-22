mylist = list(map(int, input().split()))

print(mylist)

# while True:
#     initial_command = input()
#     command_action = initial_command.split()
#
#     if command_action[0] == "exchange":
#         index = int(command_action[1])
#         if 0 < index < len(mylist):
#             new_list = mylist[index +1:] + mylist[:index +1]
#             print(new_list)
#             break
