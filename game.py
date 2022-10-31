import Bet 
import time

def come_out_phase(result):
    round=0
    print(f"Game type:Craping")
    opt_1=[7,11]
    opt_2=[2,3,12]
    if outcome in opt_2:
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll-result.bet
            time.sleep(2.5)
            print(result.update_details())
            time.sleep(2.5)
            update(result)
        elif((result.player_status==result.option[1])):
            result.bankroll=result.bankroll+result.bet
            time.sleep(2.5) 
            print(result.update_details())
    if outcome in opt_1:
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll+result.bet
            time.sleep(2.5) 
            print(result.update_details())
        else:
            if result.player_status==result.option[1]:
                result.bankroll=result.bankroll-result.bet
                time.sleep(2.5) 
                print(result.update_details())

    else:
        pass
    if (result.dice_result) in points:
        point_phase(result)
    else:
        pass
    #return(result.info())

def point_phase(result):
    print(result.update_details())
    #print(result.update_bankroll(result.bet))
    time.sleep(2.5) 
    update(result)
    #print(result.info())
    if (result.dice_result) in points:
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll+result.bet
            time.sleep(2.5) 
            print(result.update_details())
        elif(result.player_status==result.option[1]):
            result.bankroll=result.bankroll-result.bet
            time.sleep(2.5) 
            print(result.update_details())
        else:
            pass
    if (result.dice_result==7):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll-result.bet
            print(result.update_details())
        elif(result.player_status==result.option[1]):
            result.bankroll=result.bankroll+result.bet
            time.sleep(2.5) 
            print(result.update_details())
    return(result.info())




points=[4,5,6,8,9,10]
come_out=[2,3,12,7,11]
#results=Dice(2)

def main():
    result=Bet.bets()
    if result.betting_turn()=='no':
        print("Thank you")
  
    else:
        print(update(result))

def update(result):
    global outcome
    round=1
    score=0
    rolling=input("Are you ready to roll:")
    #result.information=
    if(rolling.lower().strip()=='yes'):
        roll_result=result.roll()
        #print(f"Dice result:{roll_result}")
        outcome=sum(list(roll_result))
        #print(f"Dice total:{outcome}")
        #print(type(outcome))
        if outcome in come_out:
            come_out_phase(result)
        elif outcome in points:
            point_phase(result)
        else:
            pass
        round=round+1
    else:
        pass
        

main()

            