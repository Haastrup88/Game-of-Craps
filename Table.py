import Dice
class Table(Dice.Dice):
    def __init__(self):
        super().__init__()

    def set_point(self):
        self.points=[4,5,6,8,9,10]
        if self.dice_result in self.points:
            self.point="ON"
        else:
            self.point="OFF"
            
    def point_outcome(self):
        print(f"Point_Outcome:{self.point}")
