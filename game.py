import Bet 
import time

def come_out_phase(result):
    print(f"Game type:Crapping")
    opt_1=[7,11]
    opt_2=[2,3,12]
    if result.dice_result in opt_2:
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll-result.bet
            # time.sleep(2.5)
            print(result.update_details())
            # time.sleep(2.5)
            update(result)
        elif((result.player_status==result.option[1])):
            result.bankroll=result.bankroll+result.bet
            print(result.update_details())
            start_game()
    elif (result.dice_result in opt_1):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll+result.bet
            # time.sleep(2.5) 
            print(result.update_details())
            start_game()
        else:
            if result.player_status==result.option[1]:
                result.bankroll=result.bankroll-result.bet
                # time.sleep(2.5) 
                print(result.update_details())
    else:
        pass
    if (result.dice_result) in points:
        point_phase(result)
    else:
        pass
    
   

def point_phase(result):
    if (result.dice_result != 7):
        print(result.update_details())
        print("Second phase is activated: It requires you to place odd bet")
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




points=[4,5,6,8,9,10]
come_out=[2,3,12,7,11]

def main():#The initialization function
    start_game()

def start_game():
    result=Bet.bets()
    if result.betting_turn()=='no':
        print("Thank you")
  
    else:
        print(update(result))


def odd_bets(result):
    print(point,result.dice_result)
    if (result.dice_result!=point):
        point_update(result) 
    elif(result.dice_result==point):
        if(result.dice_result==4 or result.dice_result==10):
            result.bankroll=result.bankroll+(result.bet*3)
            print(result.update_details())
        elif(result.dice_result==5 or result.dice_result==9):
            result.bankroll=result.bankroll+(result.bet*4)
            print(result.update_details())
        elif(result.dice_result==6 or result.dice_result==8):
           result.bankroll=result.bankroll+(result.bet*5)
           print(result.update_details())
        print("You Won the odd bet")

        start_game()
    else:
        pass
        







def point_update(result):
    if(point==4 or point==10):
        print(f"You are required to make 3X of your initial bet, i.e. 3*{result.bet}")
    elif(point==5 or point==9):
        print(f"You are required to make 4X of your initial bet, i.e. 4*{result.bet}")
    elif(point==6 or point==8):
        print(f"You are required to make 5X of your initial bet, i.e. 5*{result.bet}")

    else:
        pass
        
    rolling=input("Are you ready to roll, Yes/No?:")
    if(rolling.lower().strip()=='yes'):
        result.roll()
        print(result.update_details())
        if (result.dice_result==7 or result.dice_result in [2,3,11,12]):
            point_phase(result)

        elif(result.dice_result in points):
            odd_bets(result)
            
    else:
        pass


def update(result):
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

            