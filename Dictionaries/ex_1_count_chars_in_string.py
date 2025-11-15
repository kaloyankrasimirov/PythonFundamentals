chars = input()
letters = {}

for char in chars:
    if char == " ":
        continue
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for char, occurrence in letters.items():
    print(f"{char} -> {occurrence}")