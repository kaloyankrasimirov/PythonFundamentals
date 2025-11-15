days_of_adventure = int(input())
participants_number = int(input())
group_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())
total_water = water_per_day_for_one_person * days_of_adventure * participants_number
total_food = food_per_day_for_one_person * days_of_adventure * participants_number

for day in range(1, days_of_adventure +1):
    energy_loss_per_day = float(input())
    group_energy -= energy_loss_per_day

    if group_energy <= 0:
        print(
            f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    if day % 3 == 0:
        group_energy *= 1.10
        total_food -= total_food/participants_number
    if day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.70

if group_energy > 0:
    print(f"You are ready for the quest. You will be left with {group_energy:.2f} energy!")


