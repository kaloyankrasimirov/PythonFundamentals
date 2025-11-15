neighbourhood = list(map(int, input().split("@")))

print(neighbourhood)

while True:
    command = input().split()

    if command[0] == "Love":
        pass

    cupid_first_position = neighbourhood[0]
    jump_length = command[1]

    if command[0] == "Jump":

