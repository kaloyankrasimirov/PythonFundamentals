data = input().split()

inventory = {}

for i in range(0, len(data), +2):
    food = data[i]
    quantity = int(data[i + 1])
    inventory[food] = quantity

print(inventory)

