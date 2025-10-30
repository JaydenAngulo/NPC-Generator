names_list = ["Jayden", "Nick", "Joe Schmoe", "Kevin", "Gavin", "Bob", "Casper", "Mario", "Michael", "Ryan"]
import random

for names in names_list:
    HP = random.randint(0.0, 100.0)
    print(f"{names}'s HP is {HP}")

for names in names_list:
    weapon_type_options = ["melee", "sword", "ranged", "magical"]
    weapon_type = (input(f"Enter a weapon type for {names}. \nYour options are melee, sword, ranged, or magical: "))
    while weapon_type not in weapon_type_options:
        weapon_type = input("Your answer must be one of the options: ")

for names in names_list:
    speed = random.randint(1, 100)
    print(f"{names}'s speed is {speed}")