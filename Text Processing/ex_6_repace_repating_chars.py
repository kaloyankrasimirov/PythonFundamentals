the_string = input()
final_string = ""
for char in the_string:
    if not final_string or char != final_string[-1]:
        final_string += char
print(final_string)