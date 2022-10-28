from logging import exception
import random

class Dice(object):
    def __init__(self,dice1,dice2):
        self.dice1=dice1
        self.dice2=dice2
    def roll(self):
        return(f"Outcome:{self.dice1},{self.dice2}")

class Table(Dice):
    def __init__(self,dice1,dice2,point):
        super().__init__(dice1,dice2)
        self.point=point
    def point(self):
        return(f"Point:{self.point}")

class Player(Table):
    def __init__(self,dice1,dice2,point,name):
        super().__init__(dice1,dice2,point)
        self.name=name

    def bankroll(self):
        try:
          amount=input(f" {self.name}, what is your bankroll?")
        except:
            print("Bankroll must be more than 10 dollars")
            amount=0
        return(amount) 
        

    def Name(self):
        print(f"Player name is {self.name}")


print("***This is GAME OF CRAPS***")
print("**Kindly respond to the questions below;")
player=input("Enter your name:")
print(f"Welcome {player}")

result=Player(random.randint(1,6),random.randint(1,6),"Off",player)
print(result.bankroll())