def cast_spell(heroes_dict:dict, some_command:list) -> dict:
    current_hero_name, mp_needed, spell_name = some_command[1], int(some_command[2]), some_command[3]
    if heroes_dict[current_hero_name]["MP"] >= mp_needed:
        heroes_dict[current_hero_name]["MP"] -= mp_needed
        print(f"{current_hero_name} has successfully cast {spell_name} and now has {heroes_dict[current_hero_name]['MP']} MP!")
    else:
        print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")
    return heroes_dict

def take_damage(heroes_dict:dict, some_command:list) -> dict:
    current_hero_name, damage, attacker = some_command[1], int(some_command[2]), some_command[3]
    heroes_dict[current_hero_name]["HP"] -= damage
    if heroes_dict[current_hero_name]["HP"] > 0:
        print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[current_hero_name]['HP']} HP left!")
    else:
        print(f"{current_hero_name} has been killed by {attacker}!")
        del heroes_dict[current_hero_name]
    return heroes_dict

def recharge(heroes_dict:dict, some_command:list) -> dict:
    current_hero_name, amount = some_command[1], int(some_command[2])
    heroes_dict[current_hero_name]['MP'] += amount
    if heroes_dict[current_hero_name]['MP'] > 200:
        dif = heroes_dict[current_hero_name]['MP'] - 200
        healed_amount = amount - dif
        heroes_dict[current_hero_name]['MP'] = 200
        print(f"{current_hero_name} recharged for {healed_amount} MP!")
    else:
        print(f"{current_hero_name} recharged for {amount} MP!")
    return heroes_dict

def heal(heroes_dict:dict, some_command:list) -> dict:
    current_hero_name, amount = some_command[1], int(some_command[2])
    heroes_dict[current_hero_name]['HP'] += amount
    if heroes_dict[current_hero_name]['HP'] > 100:
        dif = heroes_dict[current_hero_name]['HP'] - 100
        healed_amount = amount - dif
        heroes_dict[current_hero_name]['HP'] = 100
        print(f"{current_hero_name} healed for {healed_amount} HP!")
    else:
        print(f"{current_hero_name} healed for {amount} HP!")
    return heroes_dict

heroes = {}
heroes_number = int(input())
for n in range(heroes_number):
    hero_stats = input().split()
    hero_name, hp, mp = hero_stats[0], int(hero_stats[1]), int(hero_stats[2])
    heroes[hero_name] = {"HP": hp, "MP": mp}

command = input()
while command != "End":
    command = command.split(" - ")
    action  =  command[0]
    if action == "CastSpell":
        heroes = cast_spell(heroes, command)

    elif action == "TakeDamage":
        heroes = take_damage(heroes, command)

    elif action == "Recharge":
        heroes = recharge(heroes, command)

    elif action == "Heal":
        heroes = heal(heroes, command)

    command = input()

for hero, points in heroes.items():
    print(hero)
    print(f"HP: {points['HP']}")
    print(f"MP: {points['MP']}")