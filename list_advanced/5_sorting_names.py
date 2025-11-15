list_of_names = input().split(", ")

sorted_names = sorted(list_of_names, key=lambda x: (-len(x), x))
print(sorted_names)
