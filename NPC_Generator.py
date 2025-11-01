names_list = ["Jayden", "Nick", "Joe Schmoe", "Kevin", "Gavin", "Bob", "Casper", "Mario", "Michael", "Ryan"]

import random
names_HP = {}
for names in names_list:
    HP = random.randint(1, 100)
    names_HP[names] = HP

names_health = {}
for names in names_list:
        names_health[names] = names_HP[names] >= 20

names_attack = {}
for names in names_list:
    attack_strengths = ["Very Low", "Low", "High", "Very High"]
    attack_strength = random.choice(attack_strengths)
    names_attack[names] = attack_strength

names_speed = {}
for names in names_list:
    speed = random.uniform(1, 10)
    names_speed[names] = speed

names_weapon_type = {}
for names in names_list:
    weapon_type_options = ["Melee", "Sword", "Ranged", "Magical"]
    print()
    weapon_type = (input(f"Enter a weapon type for {names}. \nYour options are melee, sword, ranged, or magical: "))
    weapon_type = weapon_type.capitalize()
    names_weapon_type[names] = weapon_type
    while weapon_type not in weapon_type_options:
        weapon_type = input("Your answer must be one of the options: ")
        weapon_type = weapon_type.capitalize()
        names_weapon_type[names] = weapon_type

import time
print()
print("These are your NPCs' attributes:")
for names in names_list:
    if names is names_list[0]:
        time.sleep(2.5)
        print()
        print(f"{names}'s attributes:\n     HP: {names_HP[names]}\n     Good Health?: {names_health[names]}\n     Attack Strength: {names_attack[names]}\n     Speed: {round(names_speed[names], 1)}\n     Weapon Type: {names_weapon_type[names]}")
    else:
        time.sleep(4)
        print()
        print(f"{names}'s attributes:\n     HP: {names_HP[names]}\n     Good Health?: {names_health[names]}\n     Attack Strength: {names_attack[names]}\n     Speed: {round(names_speed[names], 1)}\n     Weapon Type: {names_weapon_type[names]}")