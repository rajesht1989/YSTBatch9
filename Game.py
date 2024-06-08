import random
play=int(input("How many times you will paly :"))
game=["stone","paper","scissor"]
for play in range(0, play):
    choice=input("(stone or paper or scissor) : ")
    for choice in game :
        if choice==(random.choice(game)):
            print("you win")
        else:
            print("try again")
