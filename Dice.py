import random
class Dice(object):
    def __init__(self):
        self.dice1=6
        self.dice2=6
        self.dice_result=0
    def roll(self):
        self.result=((random.randint(1,self.dice1),random.randint(1,self.dice2)))
        self.dice_result=sum(list(self.result))
        return(self.result)
