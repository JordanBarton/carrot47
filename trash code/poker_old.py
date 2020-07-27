#%% poker hand exercise

#deck
    #shuffle
    #deal (to a player with removal)

#cards
    #number
    #suit
    

#TODO: deal to n players : write them in with hands as type None
#TODO: pot splitting
    
  
    
from random import shuffle
import itertools 

def findsubsets(s, n): 
    return list(itertools.combinations(s, n))

def calculate_kicker(full_hand , ranking_hand):
    #full hand list of 7 cards (1,2,3,4,4,5,6)
    #ranking hand a list of a few cards (3,4...)


    left_overs = list(filter(lambda x: x not in ranking_hand, full_hand))
 
    return max(left_overs)


def convert_card(x):
   

        if x == "ace":
            return 14
        if x == "king":
            return 13
        if x == "queen":
            return 12
        if x == "jack":
            return 11
        else:
            return x

def check_royalflush(hand):
     cards = []
     for card in hand:
         value = convert_card(card.number)
         cards.append([card.suit,value])      
     cards.sort()
     cards.pop(0)
     cards.pop(0)
     numbers=[]
     suits=[]
     for i in range(0,len(cards)):
         numbers.append(cards[i][1])
         suits.append(cards[i][0])
     suits_set = set(suits)
     if len(suits_set) == 1:
         if sum(numbers) == 60:
             print("royal flush")
             return 10
         else: 
             return 0
     else:
         return 0
    
        
         
         
     #check if there are 5 of same suit
     #check if those 5 add to 60
             
     
def check_straightflush(hand):
    
    try:
        v , hand_values = check_flush(hand)
    
        for i in hand_values:
            new_card = card(i,"na")
            total_cards.append(new_card)  
           
        flush_hand = deck(total_cards)
        value  = check_straight(flush_hand)
        
        print("straightflush")
        return value + 4 
    except: 
        return 0
    
    
#def check_4ofkind(hand):
    
#def check_fullhouse(hand):
    
def check_flush(hand):

     n_diamond=0
     n_heart =0
     n_club = 0
     n_spade = 0
     for card in hand:
         if card.suit == "diamond":
             n_diamond+=1
         if card.suit == "heart":
             n_heart +=1
         if card.suit == "club":
             n_club +=1
         if card.suit == "spade":
             n_spade +=1
    
  
     
     if n_diamond >4 or n_heart >4 or n_club >4 or n_spade > 4:

         if n_diamond > 4:
             flush_type = "diamond"
         if n_heart >4:
             flush_type = "heart"
         if n_club >4:
             flush_type = "club"
         if n_spade >4:
             flush_type = "spade"
             
         values = []
         for card in hand:
            if card.suit == flush_type:
                value = convert_card(card.number)
                values.append(value)
         
         values.sort(reverse = True)
           
        
         value = values[0]/100 + values[1]/100/100 + values[2]/100/100/100 + values[3]/100/100/100/100 + values[4]/100/100/100/100/100
             
      
         print("flush")
         return 6 + value , values
    
    
     else:
         return 0 , None
             #now flush work in a funny way for joint cases
             #highest ranking card wins + 0.05*rank
             #if same then next highest rank + 0.05*rank/100
             #if same then next highest+ 0.05 * rank/100/100
             #if same then next highest+0.05*rank/100/100/100
             #if same then last card+0.05*rank/100/100/100/100
             #if same then draw

            
   
def check_straight(hand):
  
     cards = []
     for card in hand:
         value = convert_card(card.number)
         cards.append(value)    
     cards.sort()
     cards = set(cards)
 
     temp = findsubsets(cards,5)
     straight = (0,0,0,0,0)
     old_cumsum = 0
     cumsum = 0
     for possibilites in temp:
     
         count = 0
         for i in range(0, 4):
             if possibilites[i+1] - possibilites[i] == 1:
                 count+=1
         if count == 4:
             cumsum = sum(possibilites)
             
         if possibilites == (14,2,3,4,5):
             cumsum = 28
             
         if cumsum > old_cumsum:
             straight = possibilites
             old_cumsum = cumsum
             
        
 
     #now we have a base value of 5 for straight
     #need to add extra values on the accomodate edge cases
     #cannot have value 6 
     #there are 14 possilbe straights 
     #add 0.05 * starting card value
     if cumsum !=0:
         value = 5 + 0.05*straight[0]
         print("straight")
         return value
     else:
         return 0 
         
         
         
         
   
        
     
#need to make an extra copy of first card at the end
#if an ace is followed be a 2 then 14-2 = 12 so subtract 11 more
     


    
#def check_3ofkind(hand):
    
#def check_2pair(hand):
    
def check_pairs(hand):
    pair = []
    threekind = []
    fourkind = []
    cards =[]
    for card in hand:
        value = convert_card(card.number)
        cards.append(value)
      
    
    cards.sort(reverse=True)
    unique_cards = set(cards)
    
 
    if len(unique_cards) != len(cards):
        for i in unique_cards:
          
            count = 0
            for j in cards:
             
                if i==j:
                    count+=1
                    
                
            if count==4:#four of a kind
                fourkind.append(i) 
            if count==3:#three of a kind
                threekind.append(i)
            if count==2:#pair
                pair.append(i)
                
          
            
    if fourkind!=[]:
        return 8        
            
    
    if threekind!=[]:
        
       #for full house we need to check the three of a kind then pair
       #rank based on three of kind
       #if same then rank based on pair
       if pair != []:  # three of a kind + at least 1 pair
           print("full house")
           value = max(threekind)/100 + max(pair)/100/100
           return 7 + value
       if len(threekind) == 2 : # 2 three of a kind
           print("full house")
           value = max(threekind)/100 + min(threekind)/100/100
           return 7 + value
            
       else: #then we have 3 of a kind
           print("threekind")
           value = max(threekind)/100 + calculate_kicker(cards,threekind)/100/100
           return 4 + value
       
    if threekind == []:
        if len(pair)>=2:
            
            print("2 pair")
            return 3 + max(pair)/100 + min(pair)/100/100 + calculate_kicker(cards,pair)/100/100/100
        
        
        if len(pair)==1:
            print("1 pair")
            return 2 + max(pair)/100 + calculate_kicker(cards,pair)/100/100
        else:
            return 0
        
    else:
        return 0


     
                
                
                
            
                
        

#def check_highcard(hand):

def winning_hand(hand):

   
    value1 = check_royalflush(hand)
    value2 = check_straightflush(hand)
    value3 = check_pairs(hand)
    value4 ,__= check_flush(hand)
    value5 = check_straight(hand)
    high_cards =[]
    for card in hand:
        high_cards.append(convert_card(card.number))
    value6 = max(high_cards)/100 + 1
 
    
    possible =[value1,value2,value3,value4,value5,value6]
    print(possible)
    return max(possible)
   
    
    #determine value from all of these
    

    #hand 1 is 2 cards with suit and number = set1
    #hand 2 is 2 cards with suit and number = set2
    #turn is 5 cards with suit and number
    
    #royal flush(10)
        #check for ace,king,queen,jack,10 all of same suot
    #straight flush(9)
        #check for 5 consecutive cards all of same suit
    #4 of a kind(8)
        #check for 4 cards of same number
    #full house(7)
        #check for 3 of a kind + 1 pair
    #flush(6)
        #check for 5 of same suit
    #straight(5)
        #check for 5 consecutive cards
    #three of a kind(4)
        #check for 3 cards of same number
    #2 pair(3)
        #check for 2 sets of 1 pair
    #1 pair(2)
        #check for 2 cards of same number
    #high card(1)
        #check for highest card
        
    #deciding factors if value==value: the overall value of the set
                                       #if same then value of kicker card
                                       #if same then draw
    
    
             
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
    
    
class player(deck):
    def __init__(self, cards, name, money):
        self.cards = cards
        self.name = name
        self.money = int(money)
        self.bet = 0
       
        
    def Raise(self, bet):
         old_bet = self.bet
         self.bet =   int( bet )  
         if self.bet >= self.money or self.bet <0:
             self.money = self.money -  self.money
         else:
             self.money = self.money + old_bet - self.bet

        
         return self.money
        
        
    def fold(self, bet):
        self.cards = None
        self.bet = int(bet)
    
    



suits = ["heart","diamond","club","spade"]
numbers = [2,3,4,5,6,7,8,9,10,"jack","queen","king", "ace"]


total_cards = []
for i in suits:
    for j in numbers:
        new_card = card(i,j)
        total_cards.append(new_card)

       
playing_deck = deck(total_cards)
playing_deck.show_deck()
print("\nnow shuffling\n")
playing_deck.shuffle() 


blank= player(None,"flop",0)

flop = player( [playing_deck.deal(), playing_deck.deal(), playing_deck.deal()],"flop",0 )


turn = player([flop.cards[0], flop.cards[1], flop.cards[2] , playing_deck.deal()],"turn",0)


river = player([turn.cards[0], turn.cards[1], turn.cards[2] , turn.cards[3], playing_deck.deal()],"river",0)




print("\nnow dealing\n")
player1 = player([playing_deck.deal(),playing_deck.deal()], 1, 1000)
player2 = player( [playing_deck.deal(),playing_deck.deal()], 2, 1000)
player3 = player( [playing_deck.deal(),playing_deck.deal()], 3, 1000)
player4 = player([playing_deck.deal(),playing_deck.deal()], 4, 1000)
player5 = player( [playing_deck.deal(),playing_deck.deal()], 5, 1000)
player6 = player( [playing_deck.deal(),playing_deck.deal()], 6, 1000)
player7 = player([playing_deck.deal(),playing_deck.deal()], 7, 1000)
player8 = player( [playing_deck.deal(),playing_deck.deal()], 8, 1000)

players = [player1,player2,player3,player4,
           player5,player6,player7,player8]

nplayers = 3
for i in range(0,len(players)):
    if i>nplayers:
        players[i].fold(0)


player1.Raise(1)
player2.Raise(2)
for n in range(0,4):
    
    flag = 1
    while(flag):
        

        
        
            if player3.cards == None:
                player3.fold(player2.bet)
            else:
                player3_decision = input("what will player 3 do?")
                if player3_decision == "raise":
                    player3.Raise(input("how much?"))
                if player3_decision == "fold":
                    player3.fold(player2.bet)
                if player3_decision == "call":
                    player3.Raise(player2.bet)
                    
        
            if player1.bet == player2.bet == player3.bet != 0 :
                flag = 0
                break
            

            
            
            if player1.cards == None:
                player1.fold(player3.bet)
            else:  
                player1_decision = input("what will player 1 do?")
                if player1_decision == "raise":
                    player1.Raise(input("how much?"))
                if player1_decision == "fold":
                    player1.fold(player3.bet)
                if player1_decision == "call":
                    player1.Raise(player3.bet)
    
            if player1.bet == player2.bet == player3.bet !=0:
              
                flag = 0
                break
            
            
            
            if player2.cards == None:
                player2.fold(player1.bet)
                
            else:
                player2_decision = input("what will player 2 do?")
                if player2_decision == "raise":
                    player2.Raise(input("how much?"))
                if player2_decision == "fold":
                    player2.fold(player1.bet)
                if player2_decision == "call":
                    player2.Raise(player1.bet)
    
    
            if player1.bet == player2.bet == player3.bet :
                flag = 0
                break

           

    
    if player1.cards == None:
        player1.bet = 0
    if player2.cards == None:
        player2.bet = 0
    if player3.cards == None:
        player3.bet = 0
    if n==0:
        blank.money = player1.bet + player2.bet + player3.bet
        print(blank.money)
        print("\nnow flopping\n")
        print(flop.show_deck())
        
    if n == 1:  
        flop.money =  player1.bet + player2.bet + player3.bet 
        print(flop.money)
        print(print("\nnow turning\n"))
        print(turn.show_deck())
    if n ==2:
        turn.money =  player1.bet + player2.bet + player3.bet 
        print(turn.money)
        print("\nnow riverring\n")
        print(river.show_deck())
    
    if n ==3:
        river.money = player1.bet + player2.bet + player3.bet 
        print(river.money) 
       
   

    print(player1.bet)
    print(player2.bet)
    print(player3.bet)
    print(player1.money)
    print(player2.money)
    print(player3.money)
    
    player1.bet = 0
    player2.bet = 0
    player3.bet = 0
    
    
    

print("players now show hands\n")
if player1.cards != None:
    print(player1.show_deck())
if player2.cards != None:
    print(player2.show_deck())
if player3.cards != None:
    print(player3.show_deck())








values=[]
try:
    value = winning_hand([river.cards[0], river.cards[1], river.cards[2] , river.cards[3],river.cards[4],player1.cards[0],player1.cards[1]])
except:
    value = 0
values.append(value)
    
try:
    value = winning_hand([river.cards[0], river.cards[1], river.cards[2] , river.cards[3],river.cards[4],player2.cards[0],player2.cards[1]])
except:
    value = 0
values.append(value)    

try:
    value = winning_hand([river.cards[0], river.cards[1], river.cards[2] , river.cards[3],river.cards[4],player3.cards[0],player3.cards[1]])
except:
    value = 0
values.append(value)
maxv = max(values)

for i in range(0,len(values)):
    if values[i] == maxv:
        print("player",i+1,"wins")
        
if player1.name == i:
    player1.money = player1.money + blank.money + flop.money + turn.money + river.money
if player2.name == i:
    player2.money = player2.money + blank.money + flop.money + turn.money + river.money
if player3.name == i: 
    player3.money = player3.money + blank.money + flop.money + turn.money + river.money
print(player1.money, player2.money, player3.money)                
    
        







#,[turn.cards[0], turn.cards[1], turn.cards[2] , turn.cards[3],turn.cards[4],player2.cards[0],player2.cards[1]]