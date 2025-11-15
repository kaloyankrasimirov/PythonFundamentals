current_coffees = 0

while True:
    command = input()

    if command.upper() == "END":
        break

    if command in ["cat", "dog", "movie", "coding"]:
        current_coffees += 1
    elif command in ["CAT", "DOG", "MOVIE", "CODING"]:
        current_coffees += 2
    else:
        continue

if current_coffees > 5:
    print("You need extra sleep")
else:
    print(current_coffees)

