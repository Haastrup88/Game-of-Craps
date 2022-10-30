import Dice
class Table(Dice.Dice):
    def __init__(self):
        super().__init__()

        if sum(list((self.dice1,self.dice2))) not in self.points:
            self.point="OFF"
        else:
            self.point="ON"
        
    def point_outcome(self):
        print(f"Point_Outcome:{self.point}")
