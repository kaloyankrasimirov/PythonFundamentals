queue = int(input())
lift_current_state = list(map(int, input().split()))
max_capacity = 4

for wagon in range(len(lift_current_state)):
    free = max_capacity - lift_current_state[wagon]

    if free > 0 and queue > 0:
        boarding = min(free, queue)
        lift_current_state[wagon] += boarding
        queue -= boarding

if queue == 0 and any(w < max_capacity for w in lift_current_state):
    print("The lift has empty spots!")
elif queue > 0:
    print(f"There isn't enough space! {queue} people in a queue!")

print(" ".join(map(str, lift_current_state)))