from logging import exception
import random
from unittest import result
round=1

class Dice(object):
    def __init__(self,dice1=6,dice2=6):
        self.dice1=dice1
        self.dice2=dice2
        self.diceRoll1=random.randint(1,self.dice1)
        self.diceRoll2=random.randint(1,self.dice2)
        self.points=[4,5,6,8,9,10]
    def roll(self):
        return((self.diceRoll1,self.diceRoll2))

class Table(Dice):
    def __init__(self,dice1,dice2):
        super().__init__(dice1,dice2)

        if sum(list((self.dice1,self.dice2))) not in self.points:
            self.point="OFF"
        else:
            self.point="ON"
        
    def point_outcome(self):
        print(f"Point_Outcome:{self.point}")

class Player(Table):
    def __init__(self,dice1,dice2):
        super().__init__(dice1,dice2)
        self.name=input("Enter your name:")
        while self.name==True:
            if self.name==None:
                print(self.name)
                continue
            else:
                print(f"Welcome{self.name}")
                break
        while True:
            self.bankroll=input(f" {self.name}, How much money do you have on the table?").replace("$"," ")
            try:
                self.bankroll=int(self.bankroll)
                if self.bankroll<100:
                    print("Bankroll must be at least $100")
                    continue
                else:
                    self.Total=self.bankroll
                    break
            except ValueError:
                print("Bankroll is not convertible into a dollar amount")

    def Bankroll(self):
        return(f"Your bankroll is {self.bankroll}")
        

    def Name(self):
        print(f"Player name is {self.name}")

class bets(Player):
    def __init__(self,dice1,dice2):
        super().__init__(dice1,dice2)
        self.allowable_odds=200
        self.option=["pass","don\'t pass"]
        while True:
            self.player_status=str(input("Where are you placing your bet,('Pass'/Don\'t Pass)?"))
            if(self.player_status not in self.option):
                continue
            if (self.player_status in self.option):
                 break

        if self.player_status in self.option:
            while True:
                try:
                    self.bet=int(input("How much do you want to bet:"))
                    if(self.bet>self.Total):
                        print(f"Bet must be less than your bankroll which is {self.bankroll}")
                        continue
                    else:
                        #print("Your data is as follows;")
                        self.information={"Name":self.name,"Bankroll":self.bankroll,"Bet Status":self.player_status,"Bet":self.bet}
                        break
                except ValueError:
                    print("Your wager must be an integer")
    
    def passline(self):
        if self.player_status.lower().strip()==self.option[0]:
            return(f"{self.name} Status:{self.player_status} bet")
        else:
            pass

    def do_not_pass(self):
        if self.player_status.lower().strip()==self.option[1]:
            return(f"{self.name} Status:{self.player_status} bet")
        else:
            pass
    def ingest_bet(self):
        return(f"Your bet is {self.bet}")
    def info(self):
        return(f"Status: {self.information}")
 
        


def come_out_phase():
    print(round)
    print((result.info()))
    print(f"Dealer button {result.point}")
    print(f"Craps")
    if result.player_status==result.option[0]:
        result.bankroll=result.bankroll-result.bet
        return(update())
    elif((result.player_status==result.option[1])):
        result.bankroll=result.bankroll+result.bet 
        print(result.bankroll)
    if(sum(list(result.dice_result))=='7'or sum(list(result.dice_result))=='11'):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll+result.bet
        else:
            if result.player_status==result.option[0]:
                result.bankroll=result.bankroll+result.bet
    else:
        pass
    if(sum(list(result.dice_result)) in points):
        point_phase()
    else:
        pass
    return(result.info())

def point_phase():
    print(round)
    print((result.info()))
    print(f"Dealer button: {result.point}")
    print(result.bankroll)
    update()
    if sum(list(result.dice_result)) in points:
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll+result.bet
        elif(result.player_status==result.option[1]):
            result.bankroll=result.bankroll-result.bet
        else:
            pass
    if (sum(list(result.dice_result))=='7'):
        if result.player_status==result.option[0]:
            result.bankroll=result.bankroll-result.bet
        elif(result.player_status==result.option[1]):
            result.bankroll=result.bankroll+result.bet
    return(result.info())




points=[4,5,6,8,9,10]
come_out=[2,3,12]
results=Dice(2)
def main():
    global result
    result=bets(random.randint(1,6),random.randint(1,6))
    verify=input(f"If i am correct, your information is; {result.information},yes/no:")
    if verify.lower().strip()=='yes':
        update()
    else:
        print(f"Kindly run the program again to input the correct data") 
    


def update():
    round=1
    rolling=input("Are you reading to roll:")
    if(rolling.lower().strip()=='yes'):
        print(f"Dice result:{results.roll()}")
        outcome=sum(list(results.roll()))
        print(f"Dice total:{outcome}")
        if outcome in come_out or outcome=='7':
            come_out_phase()
        elif outcome in points:
            point_phase()
        else:
            pass
        round=round+1
        

main()

            