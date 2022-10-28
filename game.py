import random

class Dice(object):
    def __init__(self,dice1,dice2):
        self.dice1=dice1
        self.dice2=dice2
    def roll(self):
        return(f"Outcome:{self.dice1},{self.dice2}")

result=Dice(random.randint(1,6),random.randint(1,6))
print(result.roll())