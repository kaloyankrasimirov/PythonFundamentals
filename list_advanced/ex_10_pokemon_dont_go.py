distance_as_integers = list(map(int, input().split()))
caught_pokemons = []

while distance_as_integers:
    index = int(input())

    element_to_remove = 0

    if index < 0:
        element_to_remove = distance_as_integers[0]
        replacement_value = distance_as_integers[-1]
        distance_as_integers[0] = replacement_value
        distance_as_integers.pop(0)
    elif index >= len(distance_as_integers):
        element_to_remove = distance_as_integers[-1]
        replacement_value = distance_as_integers[0]
        distance_as_integers[-1] = replacement_value
        distance_as_integers.pop()
    else:
        element_to_remove = distance_as_integers.pop(index)

    caught_pokemons.append(element_to_remove)

    for i in range(len(distance_as_integers)):
        if distance_as_integers[i] <= element_to_remove:
            distance_as_integers[i] += element_to_remove
        elif distance_as_integers[i] > element_to_remove:
            distance_as_integers[i] -= element_to_remove

print(sum(caught_pokemons))

