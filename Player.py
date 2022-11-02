from Table import Table


import Table 
class Player(Table.Table):
    def __init__(self):
        super().__init__()
        self.name=input("Enter your name:")
        while self.name==True:
            if self.name==None:
                print(self.name)
                continue
            else:
                print(f"Welcome{self.name}")
                break
        while True:
            self.bankroll=int(input(f" {self.name}, How much money do you have on the table?").replace("$"," "))
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
        return(f"${self.bankroll}") 
    
    def update_bankroll(self,update):
        self.bankroll+=update

    def Name(self):
        print(f"Player name is {self.name}")