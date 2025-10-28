names_list = ["Jayden", "Nick", "Joe Schmoe", "Kevin", "Gavin", "Bob", "Casper", "Mario", "Michael", "Ryan"]
import random
for names in names_list:
    strength = int(input(f"Enter the amount of strength you want {names} to have.\nThe strength value must be a whole number between 1 and 100:"))
    if strength >= 100 and strength <= 1:
        print("Your answer must be between 1 and 100")
for names in names_list:
    speed = random.randint(1, 100)
    print(f"{names}'s speed is {speed}")