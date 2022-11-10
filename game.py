import Bet 

points=[4,5,6,8,9,10]
come_out=[2,3,12,7,11]

def main():#The initialization function
    start_game()

def start_game():
    result=Bet.bets()
    if result.betting_turn()=='no':
        print(f"Thank you Player {result.name}")
  
    else:
        print(update(result))


def come_out_phase(result): # This function is invoke when the outcome of the dice is within the range of [2,3,12,7,11]
    print(f"Game type:Crapping")
    opt_1=[7,11]
    opt_2=[2,3,12]
    if result.dice_result in opt_2:
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll-result.bet
            print(f"{result.name} You Lost")
            print(result.update_details())
            update(result)
        elif((result.player_status==result.option[1])):
            result.bankroll=result.bankroll+result.bet
            print(f"{result.name} You Won")
            print(f"Thank you {result.name}")
            print(result.update_details())
            update(result)

    elif (result.dice_result in opt_1):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll+result.bet
            print(f"{result.name} You Won")
            print(f"Thank you {result.name}")
            print(result.update_details())
            update(result)
        else:
            if result.player_status==result.option[1]:
                result.bankroll=result.bankroll-result.bet
                print(f"{result.name} You Lost") 
                print(result.update_details())
                update(result)

    else:
        pass
    if (result.dice_result) in points:
        point_phase(result)
    else:
        pass
   

def point_phase(result):# This function is invoke when the outcome of the dice is within the range of [4,5,6,8,9,10]
    if (result.dice_result != 7):
        print(result.update_details())
        print("ODD BET")
        point_update(result)
    elif(result.dice_result==7):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll-result.bet
            point_update(result)
        elif(result.player_status==result.option[1]):
            result.bankroll=result.bankroll+result.bet 
            point_update(result)
        start_game()
    return(result.info())



def odd_bets(result):# This is odd bet function, and it is invoke when dice outcome is any of the point value
    print(point,result.dice_result)
    if (result.dice_result!=point and result.dice_result!=7):
        point_update(result) 
    elif(result.dice_result==point):
        result.bankroll=result.bankroll+result.bet
        result.bet_copy=result.bet
        print(result.update_details())
        print(f"{result.name},You Won from the odd bet")
        update(result)

    elif(result.dice_result==7):
        result.bankroll=result.bankroll-result.bet
        result.bet=0
        print(result.update_details())
        print(f"{result.name},You lost to odd bet")
        pass_bet(result)
    else:
        pass

def pass_bet(result):# Passline function at point phase
    pass_bet=int(input("How much do you want to bet?"))
    while(pass_bet>result.bankroll):
        try:
            pass_bet=int(input(f"Your wager must be less than ${result.bankroll}.How much do you want to bet?"))
                
        except ValueError:
            print("Your wager must be an integer")
    result.bet=pass_bet
    print(update(result))
    


def point_bet(result):
    odd_bet=int(input("How much do you want to bet? "))
    while(odd_bet>max_bet or odd_bet>result.bankroll):
        
        try:
            odd_bet=int(input(f"Your point wager must be lesser than ${max_bet}, likewise your bankroll of ${result.bankroll}.How much do you want to bet?"))        
                        
        except ValueError:
            print("Your wager must be an integer")
    result.bet=odd_bet


    
    
def point_update(result):# This function is invoke when the dice outcome isn't a 7.
    global max_bet
    if(result.bet==result.bet_copy):
        if(point==4 or point==10):
            print(f"You are required to place up to maximum bet of 3X of your initial bet, i.e.{3*result.bet}")
            max_bet=3*result.bet
            point_bet(result)
        elif(point==5 or point==9):
            print(f"You are required to place up to maximum bet of 4X of your initial bet, i.e. {4*result.bet}")
            max_bet=4*result.bet
            point_bet(result)
        elif(point==6 or point==8):
            print(f"You are required to place up to maximum bet of 5X of your initial bet, i.e. {5*result.bet}")
            max_bet=5*result.bet
            point_bet(result)

        else:
            pass
        
    rolling=input("Are you ready to roll, Yes/No?:")
    if(rolling.lower().strip()=='yes'):
        result.roll()
        print(result.update_details())

        if (result.dice_result in points or result.dice_result==7):
            odd_bets(result)

        elif (result.dice_result==7 or result.dice_result in [2,3,11,12]):
            point_phase(result)
            
    else:
        print(f"Your closing details: {result.update_details()}")
        pass




def update(result):# This function set in after the first initialization and determine if our result is come out phase or point phase
    global outcome
    global point
    rolling=input("Are you ready to roll:")
    if(rolling.lower().strip()=='yes'):
        roll_result=result.roll()
        result.set_point()
        outcome=sum(list(roll_result))
        if outcome in come_out:
            come_out_phase(result)
        elif outcome in points:
            point=outcome
            point_phase(result)
        else:
            pass
      
    else:
        print("Thank you")

        

main()

            