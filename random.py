import random
Game = ["stone","paper","scissore"]
game = random.choice(Game)
for i in range (0,3):
    user_value = input("Enter your choice in (stone/paper/scissore) : ").lower()
    if game == user_value:
        print("you win")
        break
    else:
        print("Try again")
        continue
