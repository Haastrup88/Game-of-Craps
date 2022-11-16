from Table import Table


import Table 
class Player(Table.Table):
    def __init__(self):
        super().__init__()
        self.name=input("Enter your name:")
        self.bankroll=int(input(f" {self.name}, How much money do you have on the table($)?").replace("$"," "))
        while(self.bankroll<100): 
            try:
                print("Bankroll must at least $100 ")
                self.bankroll=int(input(f" {self.name}, How much money do you have on the table?").replace("$"," "))
                    
            except ValueError:
                print("Bankroll is not convertible into a dollar amount")
        self.Total=self.bankroll

    def Bankroll(self):
        return(f"${self.bankroll}") 
    
    def update_bankroll(self,update):
        self.bankroll+=update

    def Name(self):
        print(f"Player name is {self.name}")