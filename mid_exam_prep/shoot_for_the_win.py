target_sequence = list(map(int, input().split()))
hit_targets = 0

while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {hit_targets} -> {' '.join(map(str, target_sequence))}")
        break

    target_index = int(command)


    if target_index not in range(len(target_sequence)):
            continue
    else:
        target_value = target_sequence[target_index]
        target_sequence[target_index] = -1

        for index in range(len(target_sequence)):
            if target_sequence[index] != -1:
                if target_sequence[index] > target_value:
                    target_sequence[index] -= target_value
                else:
                    target_sequence[index] += target_value
        hit_targets += 1


