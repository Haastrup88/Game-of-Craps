import Player 
class bets(Player.Player):
    def __init__(self):
        super().__init__()
        self.allowable_odds=200
        self.option=["pass","don\'t pass"]
        self.player_status=" "
        #return(self.bet())

    def betting_turn(self):
        while True:
            betting=input("Do you want to place a bet? yes/no:")
            if betting.lower().strip()=="yes":
                player_status=input("Where are you placing your bet,(Pass/ Don\'t Pass)?")
                if(player_status.lower().strip() not in self.option):
                    print("Invalid Input")
                    continue
                else:
                    #(player_status.lower().strip() in self.option)   
                    if player_status.lower().strip()==self.option[0]:
                        self.player_status=self.option[0]
                        print(self.bet())
                        break
                    else:
                        self.player_status=self.option[1]
                        print(self.bet())
                        break
            else:
                break
        return(betting)
    
        
    def bet(self):
        self.bet=int(input("How much do you want to bet?"))
        while(self.bet>self.Total):
            try:
                self.bet=int(input(f"Your wager must be less than ${self.bankroll}.How much do you want to bet?"))

                #print(self.insufficient_fund())
                
            except ValueError:
                    print("Your wager must be an integer")
        self.bet_copy=self.bet
        return(f"Your wager is ${self.bet}")
    

    
    def passline(self):
        self.player_status=self.option[0]
        return(f"Bet type: {self.player_status}")

    def do_not_pass(self):
        self.player_status=self.option[1]
        return(f"Bet type: {self.player_status}")

    def ingest_bet(self):
        return(f"Your bet is {self.bet}")
        
    def info(self):
        #print(f"Your bet is{self.bet}, and type is {type(self.bet)}")
        return(f"Status: {self.information}")
    
    def insufficient_fund(self):
        return((f"{self.name},Bet must be less than your bankroll which is {self.bankroll}"))
    
                
    def information(self):
        return({"Name":self.name,"Bankroll":self.bankroll,"Bet Status":self.betting_turn(),"Bet":self.bet})

    def update_details(self):
        info_update={"Name":self.name,"Closing Balance":self.Bankroll(),"Bet Status":self.player_status,"Bet":self.bet,"Dealer Status":self.point,"Dice result":self.result}
        return(info_update)

    
    
 