import time
from random import shuffle
from matplotlib import pyplot as plt
from PIL import Image
from operator import attrgetter
import os.path

    

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

        
    def save(self,player_number,card_number):
        image = Image.open("C:/Users/username/OneDrive/poker/cards/{}_{}.jpg".format(str(self.number),str(self.suit)) ) 
        image.save("C:/Users/username/OneDrive/poker/player{}/card{}.jpg".format(str(player_number),
                                                                                card_number))
       
        
  
class player(deck):
    def __init__(self, cards, name, money):
        self.cards = cards
        self.name = name
        self.money = int(money)
        
    def write_inputs(self):
        open("C:/Users/username/Desktop/players/player"+str(player.name)+"/call.txt","w")
        open("C:/Users/username/Desktop/players/player"+str(player.name)+"/raise.txt","w") 
        open("C:/Users/username/Desktop/players/player"+str(player.name)+"/fold.txt","w") 
        
    def check_inputs(self):
        call = os.path.exists("C:/Users/username/Desktop/players/player"+str(player.name)+"/call.txt")
        Raise =os.path.exists("C:/Users/username/Desktop/players/player"+str(player.name)+"/raise.txt") 
        fold = os.path.exists("C:/Users/username/Desktop/players/player"+str(player.name)+"/fold.txt") 
        if call and Raise and fold == True:
            time.sleep(0.5)
            return None
        else:
            
            if call == False:
                os.remove("C:/Users/username/Desktop/players/player"+str(player.name)+"/raise.txt") 
                os.remove("C:/Users/username/Desktop/players/player"+str(player.name)+"/fold.txt") 
                return "call"
            
            if fold == False:
                os.remove("C:/Users/username/Desktop/players/player"+str(player.name)+"/raise.txt") 
                os.remove("C:/Users/username/Desktop/players/player"+str(player.name)+"/call.txt") 
                return  "fold"
            
            if Raise == False:
                os.remove("C:/Users/username/Desktop/players/player"+str(player.name)+"/call.txt")
                os.remove("C:/Users/username/Desktop/players/player"+str(player.name)+"/fold.txt") 
                file4 = open("C:/Users/username/Desktop/players/player"+str(player.name)+"/amount.txt","w")
                file4.close()
                return "raise"
            
    def check_raise(self):
                file5 = open("C:/Users/username/Desktop/players/player"+str(player.name)+"/amount.txt","r")
                time.sleep(5)
                amount = file5.read()
                file5.close()
                time.sleep(5)
                os.remove("C:/Users/username/Desktop/players/player"+str(player.name)+"/amount.txt" )
                        
                try: 
                    amount = int(amount)
                    if  0 < amount < int(self.money):
                
                        return amount
                    else:
                        return 0
                    
                except:
                    return 0
                
        
        
suits = ["heart","diamond","club","spade"]
numbers = [2,3,4,5,6,7,8,9,10,"jack","queen","king", "ace"]


total_cards = []
for i in suits:
    for j in numbers:
        new_card = card(i,j)
        total_cards.append(new_card)

       
playing_deck = deck(total_cards)
print("\nnow shuffling\n")
playing_deck.shuffle() 



buy_in = 1000

player1 = player([playing_deck.deal(),playing_deck.deal()],  1, buy_in)
player2 = player([playing_deck.deal(),playing_deck.deal()],  2, buy_in)
players = [player1,player2]

for player in players:
    player.write_inputs()
    
   
    action = None
    while action == None:
        action = player.check_inputs()
    print(action)
    amount = 0
    if action == "raise":
        while amount == 0:
            amount  = player.check_raise()
            
    print(amount)


