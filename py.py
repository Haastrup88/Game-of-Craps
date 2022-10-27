import random


print("Welcome to GAME OF CRAPS text_based game")
print(" ")
print("*****Game Instructions****")
print("This involve two players, and both players have to provide thier names")
print(" ")
player1=input("Player One! Kindly provide your name:")
player2=input("Player Two! Kindly provide your name:")

print(f"Welcome! {player1} and {player2}")



def shooters():
    player1_score=0
    player2_score=0
    round=1
    while round!=3:
        player=input(f"First shooter? {player1} or {player2}:")
        if player.lower().strip()==player1:
            shooter=player1
        elif(player.lower().strip()==player2):
            shooter=player2
        else:
            print("Invalid Input")
        round=round+1
        return shooter


def dice_roll():
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    result=(dice_1,dice_2)
    return(result)

shooters()