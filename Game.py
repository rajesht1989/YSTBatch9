import random
Game = ["stone","paper","scissore"]
try:
    user_time = int(input("Enter your time limit : "))
    if user_time < 0 :
        raise ValueError ("Time is cannot be negative")
    for j in range (user_time+1):
            break
except Exception as e:
    print("something",e)

for i in range (0,user_time):
    game = random.choice(Game)
    user_value = input("Enter your choice in (stone/paper/scissore) : ").lower()
    if game == user_value:
        print("you win")
        continue
    else:
        print("Try again")
        continue
