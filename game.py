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
            self.point="Off"
        else:
            self.point="On"
    def point_outcome(self):
        print(f"Point_Outcome:{self.point}")

class Player(Table):
    def __init__(self,dice1,dice2,name):
        super().__init__(dice1,dice2)
        self.name=name
        #self.bankroll=bankroll

        self.bankroll=input(f" {self.name}, How much money they have on the table?").replace("$"," ")
        try:
            self.bankroll=int(self.bankroll)
            if self.bankroll<100:
                print("Bankroll must be at least $100")
        except ValueError:
            print("bankroll is not convertible into a dollar amount")



    def Bankroll(self):
        return(f"Your bankroll is {self.bankroll}")
        

    def Name(self):
        print(f"Player name is {self.name}")

def main():

    print("***This is GAME OF CRAPS***")
    print("**Kindly respond to the questions below;")
    player=input("Enter your name:")
    print(f"Welcome {player}")


    result=Player(random.randint(1,6),random.randint(1,6),player)
    print(result.roll())
    print(result.point_outcome())
    print(result.Bankroll())
main()