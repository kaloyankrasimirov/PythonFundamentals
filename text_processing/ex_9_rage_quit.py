some_string = input()
final_string = ""
sub_string = ""
repetition = ""
for index in range(len(some_string)):
    #case where we have non numeric symbol
    if not some_string[index].isdigit():
        sub_string += some_string[index].upper()
    #case where we have digit

    else:
        repetition += some_string[index]
        if index + 1 < len(some_string):
            if some_string[index +1].isdigit():
                repetition += some_string[index +1]
        final_string += int(repetition) * sub_string.upper()
        sub_string = ""
        repetition = ""
print(f"Unique symbols used: {len(set(final_string))}")
print(final_string)