some_string = input()
final_string = ""
strength = 0

for index in range(len(some_string)):
    #explosion
    if strength > 0 and some_string[index] != ">":
        strength -= 1
    #explosion marker
    elif some_string[index] == ">":
        final_string += ">"
        strength += int(some_string[index + 1])
    #no explosion and no explosion marker
    else:
        final_string += some_string[index]

print(final_string)