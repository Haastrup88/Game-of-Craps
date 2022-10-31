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
            # time.sleep(2.5) 
            print(result.update_details())
    elif (result.dice_result in opt_1):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll+result.bet
            # time.sleep(2.5) 
            print(result.update_details())
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
        point_update(result)
    elif(result.dice_result==7):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll-result.bet
            print(result.update_details())
        elif(result.player_status==result.option[1]):
            result.bankroll=result.bankroll+result.bet 
            print(result.update_details())
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


def point_update(result):
    while True:
        rolling=input("Are you ready to roll:")
        if(rolling.lower().strip()=='yes'):
            result.roll()
            result.set_point()
            if result.dice_result==7:
                point_phase(result)
            else:
                print(result.update_details())
            
        else:
            pass
        

def update(result):
    global outcome
    rolling=input("Are you ready to roll:")
    if(rolling.lower().strip()=='yes'):
        roll_result=result.roll()
        result.set_point()
        outcome=sum(list(roll_result))
        if outcome in come_out:
            come_out_phase(result)
        elif outcome in points:
            point_phase(result)
        else:
            pass
      
    else:
        pass
        

main()

            