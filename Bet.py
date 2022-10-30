import Player 
class bets(Player.Player):
    def __init__(self):
        super().__init__()
        self.allowable_odds=200
        self.option=["pass","don\'t pass"]
        while True:
            self.player_status=str(input("Where are you placing your bet,('Pass'/Don\'t Pass)?"))
            if(self.player_status not in self.option):
                continue
            if (self.player_status in self.option):
                 break

        if self.player_status in self.option:
            while True:
                try:
                    self.bet=int(input("How much do you want to bet:"))
                    if(self.bet>self.Total):
                        print(f"Bet must be less than your bankroll which is {self.bankroll}")
                        continue
                    else:
                        #print("Your data is as follows;")
                        self.information={"Name":self.name,"Bankroll":self.bankroll,"Bet Status":self.player_status,"Bet":self.bet}
                        break
                except ValueError:
                    print("Your wager must be an integer")
    
    def passline(self):
        if self.player_status.lower().strip()==self.option[0]:
            return(f"{self.name} Status:{self.player_status} bet")
        else:
            pass

    def do_not_pass(self):
        if self.player_status.lower().strip()==self.option[1]:
            return(f"{self.name} Status:{self.player_status} bet")
        else:
            pass
    def ingest_bet(self):
        return(f"Your bet is {self.bet}")
        
    def info(self):
        #print(f"Your bet is{self.bet}, and type is {type(self.bet)}")
        
        return(f"Status: {self.information}")
    def update_details(self):
        info_update={"Name":self.name,"Bankroll":self.bankroll,"Bet Status":self.player_status,"Bet":self.bet,"Dealer Status":self.point,"Dice result":self.result}
        return(info_update)
 