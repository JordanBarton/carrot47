from random import shuffle         
class deck():
    cards = []
    
    def __init__(self,cards):
        self.cards = cards
        
        
    def show_deck(self):
        components = []
        for card in self.cards:
            components.append([card.suit, card.number])
        
        return components
            
            
    def shuffle(self):
        shuffle(self.cards)
        return self
    
    def deal(self):
        return self.cards.pop(len(self.cards)-1) 
        


class card():
    
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number 
        
    def show_card(self):
        return "{} of {}".format(self.suit,self.number)
    def show_suit(self):
        return self.suit
    def show_number(self):
        return self.number
    def place_on_table(self,coords,scale):

        image = pygame.image.load("C:/Users/username/OneDrive/poker/cards/{}_{}.jpg".format(str(self.number),str(self.suit)) ) 
        image = pygame.transform.scale(image, (111*scale, 169*scale))
        display_surface.blit(image,coords)
        pygame.event.pump()
        pygame.display.update()
        
    def save(self,player_number,card_number):
        image = Image.open("C:/Users/username/OneDrive/poker/cards/{}_{}.jpg".format(str(self.number),str(self.suit)) ) 
        image.save("C:/Users/username/OneDrive/poker/player{}/card{}.jpg".format(str(player_number),
                                                                                card_number))
       
        
  
class player(deck):
    def __init__(self, cards, name, money):
        self.cards = cards
        self.name = name
        self.money = int(money)
        self.bet = 0
        self.all_in = False
        self.potential_winnings = 0
        self.score = 0
       
        
    def Raise(self, bet):
         old_bet = self.bet
         self.bet =   int( bet )  
         if self.bet >= self.money:
             self.bet = self.money
             self.money = 0
             self.all_in = True
         else:
             self.money = self.money + old_bet - self.bet

        
         return self.money
        
    def small_blind(self):
        self.Raise(1)
        
    def big_blind(self):
        self.Raise(2)
        
        
        
        
    def fold(self, bet):
        self.cards = None
        self.bet = int(bet)
        
    
 
    
    










#need to find out the pots depending on who wins

    #how do we distribute this money?
    #3 players A,B,C bet 25,50,100
    #C doesn't need to bet over 50 so takes 50 back immediately
    #25 for all players goes into pot 1 making a total of 75 which A,B,C compete for
    #25 from B and C go into a seperate pot that only they can compete for
    #so if player.Raise(x) > 2nd richest player.money -> give player difference back
    #if player.call yields player1.money then produce a pot that is n*bet
    #relevent players then compete for relvent pots
    
    #A ,B  ,C  ,D  ,E  ,F  ,G
    #50,90,120,150,180,210,1000 
    ##player G goes all in with 1000 ->210 instantly
    # #50,90,120,150,180,210,210
    #1: -50 -> 0,70,110,140,160,160       => 50*6 = 300
    #2: -40 ->    0,70,100,120,120        => 40*5 = 200
    #3: -70 ->       0,30 ,90 ,90         => 70*4 = 280
    #4: -30 ->           0,60,60          => 30*3 = 90
    #5: -60 ->              0,0           => 60*2 = 120
    #G all in too much ->takes back 700
    
    #pot1: A,B,C,D,E,F,G compete for 300
    #pot2:   B,C,D,E,F,G compete for 200
    #pot3:       D,E,F,G compete for 280
    #pot4:         E,F,G compete for 90
    #pot5:           F,G compete for 120
    #so A,B,C,D,E,F can win a maximum of 300,500,780, 870, 990,990 respectively


def pot_split():
    bets = []
    maxv=0
    for player in players:
        bets.append([player,player.bet])
        if player.money > maxv:
            maxv = player.money
        
    bets.sort(key = lambda tup: tup[1])
   
    players_in_pots =[]
    pots = []
    N = len(bets)
    for i in range(0,N):
        pot_increment = bets[i][1]

        row = []
        for j in range(0,N):
            bets[j][1] = bets[j][1] - pot_increment
        
            if bets[j][1]>=0:
                row.append(bets[j][0])
                
        players_in_pots.append(row)
        pots.append(len(row)*pot_increment)
     
       
        N = len(bets)
    print(pots)
 
    return pots,players_in_pots
       
            
    
    
        
def distribute_winnings(pots,players_in_pots):   
    #if player in higher pot wins, he wins all pots below
    N = len(pots)
    for i in range(0,N):
        players[i].money =  players[i].money - players[i].bet
        max_score = 0
        row_length = len(players_in_pots[i])
       
        for j in range(0,row_length):
         
                
            
            
            if players_in_pots[i][j].score > max_score:
                max_score = players_in_pots[i][j].score
        
        winners = []
        for j in range(0,row_length):
            if players_in_pots[i][j].score == max_score:
                winners.append(players_in_pots[i][j])
            
            
        for j in range(0,len(winners)):
          
            winners[j].money = winners[j].money + pots[i]/len(winners)
                

                
            
                
            
            
        
    
    
    
    
    
    
    
    
    


player1 = player(None, 1, 100)
player2 = player( None, 2, 200)
player3 = player(None, 3, 50)
player4 = player(None, 4, 400)
player5 = player( None, 5, 1000)
player6 = player( None, 6, 400)
player7 = player(None, 7, 600)
player8 = player(None, 8, 550)
players = [player1,
           player2,
           player3,
           player4,
           player5,
           player6,
           player7,
           player8]
player1.bet = 100
player2.bet = 200
player3.bet = 50
player4.bet = 400
player5.bet = 1000
player6.bet = 400
player7.bet = 600
player8.bet = 550

player1.score = 1
player2.score = 2
player3.score = 5
player4.score = 4
player5.score = 1
player6.score = 4
player7.score = 6
player8.score = 6



pots , players_in_pots = pot_split()

#then work out who wins
distribute_winnings(pots,players_in_pots)

#troubleshoot this
for player in players:
    print(player.score,player.money)
    
    
    
    
    
    
    