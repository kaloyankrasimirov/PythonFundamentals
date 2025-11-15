days_of_adventure = int(input())
participants_number = int(input())
group_energy = float(input())
water_per_day_for_one_person = float(input())
food_per_day_for_one_person = float(input())

# Initial supplies calculation
total_water = water_per_day_for_one_person * days_of_adventure * participants_number
total_food = food_per_day_for_one_person * days_of_adventure * participants_number

# Use 'day_index' to run the loop exactly N times (reading N inputs).
for day_index in range(days_of_adventure):

    # 1. READ ENERGY LOSS (DAILY)
    energy_loss_per_day = float(input())

    # Define the current day number (1, 2, 3...) based on the index
    # This is critical for the modulo checks (day % 2 and day % 3)
    day = day_index + 1

    # 1A. CHOP WOOD (DAILY LOSS)
    group_energy -= energy_loss_per_day

    # 1B. CRITICAL FAILURE CHECK
    if group_energy <= 0:
        # Use :.2f for the provisions in the failure message
        print(
            f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        break

    # 2. DRINK WATER (Every second day) - Must be an 'if'
    if day % 2 == 0:
        # Energy boost by 5%
        group_energy *= 1.05
        # Water supply reduced by 30%
        total_water *= 0.70

    # 3. EAT MEAL (Every third day) - Must be an 'if'
    if day % 3 == 0:
        # Energy boost by 10%
        group_energy *= 1.10

        # Food consumption: currentFood / participants_number
        food_consumed = total_food / participants_number
        total_food -= food_consumed

# FINAL SUCCESS CHECK (Outside the loop)
if group_energy > 0:
    # Use :.2f for the final energy amount
    print(f"You are ready for the quest. You will be left with {group_energy:.2f} energy!")
