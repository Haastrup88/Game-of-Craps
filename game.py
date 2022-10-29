from logging import exception
import random
round=1

class Dice(object):
    def __init__(self,dice1,dice2):
        self.dice1=dice1
        self.dice2=dice2
        self.dice_result=((self.dice1,self.dice2))
        self.points=[4,5,6,8,9,10]
    def roll(self):
        self.dice1=(self.dice1)
        self.dice2=(self.dice2)
        return(f"Dice Outcome:{self.dice_result}")

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
    def __init__(self,dice1,dice2,name):
        super().__init__(dice1,dice2)
        self.name=name
    
        #self.bankroll=bankroll

        while True:
            self.bankroll=input(f" {self.name}, How much money they have on the table?").replace("$"," ")
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
    def __init__(self,dice1,dice2,name):
        super().__init__(dice1,dice2,name)
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
    def status(self):
        pass

def come_out_phase():
    print("This is come out phase")

def point_phase():
    print("This is point out phase")


def main():
    print("***This is GAME OF CRAPS***")
    print("**Kindly respond to the questions below;")
    player=input("Enter your name:")
    print(f"Welcome {player}")


    result=bets(random.randint(1,6),random.randint(1,6),player)
    points=[4,5,6,8,9,10]
    come_out=[2,3,12]
    round=1
    while(result.bet<result.Total):
        rolling=input("Are you reading to roll:")
        if(rolling.lower().strip()=='yes'):
            if result.player_status[0]==True:
                come_out_phase()
            else:
                point_phase()
            round=round+1
        else:
            print(f"Thank you, your finishing status is {result.information} after {round} rounds")
            break
            
            
        

    
    
main()