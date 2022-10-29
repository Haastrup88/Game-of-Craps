from logging import exception
import random

class Dice(object):
    def __init__(self,dice1,dice2):
        self.dice1=dice1
        self.dice2=dice2
        self.points=[4,5,6,8,9,10]
    def roll(self):
        return(f"Dice Outcome:{self.dice1},{self.dice2}")

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
    
    def passline(self):
        if self.player_status==self.option[0]:
            return(f"{self.name} Status:{self.player_status} bet")
        else:
            pass
    def do_not_pass(self):
        if self.player_status==self.option[1]:
            return(f"{self.name} Status:{self.player_status} bet")
        else:
            pass
    def oddbet(self):
        pass
    def insufficient_fund(self):
        pass

def main():

    print("***This is GAME OF CRAPS***")
    print("**Kindly respond to the questions below;")
    player=input("Enter your name:")
    print(f"Welcome {player}")


    result=bets(random.randint(1,6),random.randint(1,6),player)
    print(result.roll())
    print(result.point_outcome())
    print(result.Bankroll())
    print(result.passline())
    print(result.do_not_pass())
    
main()