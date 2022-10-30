import Dice
class Table(Dice.Dice):
    def __init__(self):
        super().__init__()
        self.points=[4,5,6,8,9,10]

        if self.dice_result in self.points:
            self.point="OFF"
        else:
            self.point="ON"
        
    def point_outcome(self):
        print(f"Point_Outcome:{self.point}")
