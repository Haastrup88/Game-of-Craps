import random

player1_wager=500
player2_wager=500
player1_win=0
player2_win=0

def come_out_phase():
    shooter1=shooters()
    print(shooter1[0])
    

    

def shooters():
    shooter=" "
    info=[]
    player1_bet=" "
    player2_bet=" "
    round=1
    while round!=3:
        print("***ROUND*** "+str(round))
        print("Kindly know that 'P1' and 'P2' represent the first and second player")
        gambler=input("Who will go first; p1/p2?")
        if gambler.lower().strip()=="p1":
            shooter=player1
        elif(gambler.lower().strip()=='p2'):
            shooter=player2
        else:
            print("Invalid Input")
        print("In placing your bet, kindly note this;")
        print("'PL' stands for Pass line bet")
        print("'DP' stands for Don\'t pass bet")

        bet=input(f"{shooter},kindly place your bet(PL/DL):")
        if bet.lower().strip()=="pl":
            player1_bet="PL"
            player2_bet="DL"
        elif(bet.lower().strip()=="dl"):
            player1_bet="DL"
            player2_bet="PL"
        else:
            print("Invalid Input")
        round=round+1
        info.append([shooter,player1_bet,player2_bet])
        return(info[0])

def dice_roll():
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    result=(dice_1,dice_2)
    return(result)

print("Welcome to GAME OF CRAPS text_based game")
print(" ")
print("*****Game Instructions****")
print("This involve two players, and both players have to provide thier names")
print(" ")
player1=input("Player One! Kindly provide your name:")
player2=input("Player Two! Kindly provide your name:")

print(f"Welcome! {player1} and {player2}")

shooters()
come_out_phase()