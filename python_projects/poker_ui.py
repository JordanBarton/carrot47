# import pygame module in this program 
import pygame 
import time
from matplotlib import pyplot as plt
from PIL import Image
from operator import attrgetter





def button(msg,x,y,width,height,colour_on,colour_off):
          
    font = pygame.font.Font('freesansbold.ttf', 32) 
  
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+width>mouse[0]>x and y+width>mouse[1]>y:
        pygame.draw.rect(display_surface,colour_on,(x,y,width,height)) 
       
        if click[0] == 1:
            time.sleep(0.1)
            return True
        
        
    else:
        pygame.draw.rect(display_surface,colour_off,(x,y,width,height)) 
        

 
    
    
  
    # create a text suface object, 
    # on which text is drawn on it. 
    text = font.render(msg, True, white) 
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
      
    # set the center of the rectangular object. 
    textRect.center = (x+(width// 2), y  + (height// 2)) 
    display_surface.blit(text, textRect)
    
  
    
#%% set up pygame ui    
# activate the pygame library 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# define the RGB value for white, 
#  green, blue colour . 
black = (0,0,0)
white = (255, 255, 255) 
green = (0, 200, 0) 
red = (200,0,0)
bright_red = (255,0,0)
bright_green=(0,255,0)

block_colour = (53,155,255)

car_width = 73
# assigning values to X and Y variable 
X = 1920
Y = 1080
  
# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('Show Text') 
  
# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
display_surface.fill(white) 
# infinite loop 

#location of all objects to be placed on screen
player1_card1=(300, 200)
player2_card1=(450, 200)
player3_card1=(600, 200)
player4_card1=(750, 200)
player5_card1=(900, 200)
player6_card1=(1050, 200)
player7_card1=(1200, 200)
player8_card1=(1350,200)
player1_card2=(300, 400)
player2_card2=(450, 400)
player3_card2=(600, 400)
player4_card2=(750, 400)
player5_card2=(900, 400)
player6_card2=(1050, 400)
player7_card2=(1200, 400)
player8_card2= (1350,400)
player_location_card1 = [player1_card1,
                         player2_card1,
                         player3_card1,
                         player4_card1,
                         player5_card1,
                         player6_card1,
                         player7_card1,
                         player8_card1]
player_location_card2 = [player1_card2,
                         player2_card2,
                         player3_card2,
                         player4_card2,
                         player5_card2,
                         player6_card2,
                         player7_card2,
                         player8_card2]



table_card1=(300, 700)
table_card2=(550, 700)
table_card3=(800, 700)
table_card4=(1050, 700)
table_card5=(1300,700)

table_location_card=[table_card1,
                     table_card2,
                     table_card3,
                     table_card4,
                     table_card5]

nametag = [300,450,600,750,900,1050,1200,1350]

    
  
    
    
    

#%% poker hand exercise

#deck



    
 
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
    
 
def pot_split():
    bets = []
    maxv=0
    for player in players:
        bets.append([player,player.bet])
        if player.bet > maxv:
            maxv = player.bet
        
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
  
 
    return pots,players_in_pots
       
            
    
    
        
def distribute_winnings(pots,players_in_pots):   
    #if player in higher pot wins, he wins all pots below
    N = len(pots)
    print(pots)
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
      
        
def get_max_bet(players):
    return max(players, key = attrgetter('bet')).bet
 #%% define classes   
    
    
             
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
        self.score = 0
        self.fold = False
        self.buy_in = 0
       
        
    def Raise(self, bet):
       #  old_bet = self.bet
         self.bet  =   int( bet )  
         if self.bet >= self.money:
             self.bet = self.money
             self.all_in = True
       #      self.money = 0
       #      self.all_in = True
        # else:
            # self.money = self.money + old_bet - self.bet
 
        
    def small_blind(self):
        self.Raise(1)
        
    def big_blind(self):
        self.Raise(2)
        
    def fold_player(self):
        self.cards = None
        self.fold = True
        

       
    
    
 
    
    
#%% set up game


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


blank= player(None,"flop",0)

flop = player( [playing_deck.deal(), playing_deck.deal(), playing_deck.deal()],"flop",0 )

turn = player([flop.cards[0], flop.cards[1], flop.cards[2] , playing_deck.deal()],"turn",0)

river = player([turn.cards[0], turn.cards[1], turn.cards[2] , turn.cards[3], playing_deck.deal()],"river",0)


#need a more elegent way of writing this
nplayers = 4#max 8
buy_in = 1000
blind_amounts = [1,2]
player1 = player([playing_deck.deal(),playing_deck.deal()],  "jordan", buy_in)
player2 = player( [playing_deck.deal(),playing_deck.deal()], 2, buy_in)
player3 = player( [playing_deck.deal(),playing_deck.deal()], 3, buy_in)
player4 = player([playing_deck.deal(),playing_deck.deal()],  4, buy_in)
player5 = player( [playing_deck.deal(),playing_deck.deal()], 5, buy_in)
player6 = player( [playing_deck.deal(),playing_deck.deal()], 6, buy_in)
player7 = player([playing_deck.deal(),playing_deck.deal()],  7, buy_in)
player8 = player( [playing_deck.deal(),playing_deck.deal()], 8, buy_in)




players = [player1,player2,player3,player4,
           player5,player6,player7,player8]


cycle=[]
#get rid of players that aren't playing and produce the turn order
for i in range(0,len(players)):
        if i>=nplayers:
            players[i].fold_player()
        if i <nplayers:#0,1,2,3
            cycle.append(i)



#%% play the game

game = True
while game == True:#starts with player 7,8    ,1,2 etc....

   
        
    dealer = cycle[len(cycle) - 3]
    small_blind = cycle[len(cycle)-2]
    big_blind = cycle[len(cycle) - 1]

    #give players an attribute small blind or big blind
    
    
    
    b = button("pot: £0 ",10,450,250,32,black,black) 
    for i in range(0,len(players)):

        if cycle.count(i) == 0:#if i is not in cycle
            players[i].fold_player()
        if cycle.count(i) == 1 and players[i].money !=0:#if i is in cycle

            button(" {}".format(players[i].name),
                   nametag[i],50,
                   130,32,black,black)
            button("£{}/{}".format(0,int(players[i].money)),
                                   nametag[i],100,
                                   130,32,
                                   black,black)
            
    

    players[small_blind].small_blind()
    players[big_blind].big_blind()
    
    button("£{}/{}".format(int(players[small_blind].bet),int(players[small_blind].money)),
                                   nametag[small_blind],100,
                                   130,32,
                                   black,black)
                
    button("£{}/{}".format(int(players[big_blind].bet),int(players[big_blind].money)),
                                   nametag[big_blind],100,
                                   130,32,
                                   black,black)
    button("s", nametag[small_blind]+50,0,
                                   20,32,
                                   black,black)
                
    button("b", nametag[big_blind]+50,0,
                                   20,32,
                                   black,black)
    
    button("d", nametag[dealer]+50,0,
                                   20,32,
                                   black,black)
    
    
   

    for i in range(0,nplayers):
            if players[i].cards != None:
                players[i].cards[0].save(i+1,1)
                players[i].cards[1].save(i+1,2)
    
    
    
    nfold = 0
    for n in range(0,  4):
      
        number_of_calls = 0
        flag = 1
        while(flag == 1):


                for i in range(0,nplayers):
                    whos_turn = cycle[i]
                    print("turn ",whos_turn + 1)
                    
                    
                    if n==0 and i ==0 :
                      
                        previous = cycle[nplayers - 1]
                    else:
                        previous = cycle[i-1]
    
                    if players[i].cards == None:
                        players[i].fold_player()
                    else:
                       
                    
                        button("{}".format(players[whos_turn].name),
                               nametag[whos_turn],50,
                               130,32,green,green)
                        pygame.event.pump()
                        pygame.display.update()
                    
                          

                        pygame.event.pump()
                        pygame.display.update()
                    
                        pressed = False
                        while pressed == False:
                            if players[whos_turn].all_in == True or players[whos_turn].fold == True:
                                decision = ""
                                players[whos_turn].Raise(0)
                                pressed = True
                            else:
                            
                                pygame.event.pump()
                                pygame.display.update()
                                call = button("call",100,100,100,100,green,red)
                                Raise = button("raise",100,200,100,100,green,red)
                                fold = button("fold",100,300,100,100,green,red)
                                QUIT = button("quit",100,600,100,100,green,red)
                                
                            if call  == True: 
                                decision = "call"
                                pressed=True
                                
                            if Raise  == True: 
                                decision = "raise"
                                pressed=True
                                
                            if fold  == True: 
                                decision = "fold"
                                pressed=True
                                nfold += 1
                                
                            if QUIT == True:
                                pygame.quit()
                                quit()
            
                        pygame.event.pump()
                        pygame.display.update()
                        if decision == "raise":
                            Raise_amount = input("how much?")
                            if int(Raise_amount) < get_max_bet(players):
                                players[whos_turn].Raise(get_max_bet(players))
                                number_of_calls +=1
                            else:
                                players[whos_turn].Raise(Raise_amount)
                                number_of_calls = 1
                                
                        if decision == "fold":
                            players[whos_turn].fold_player()
                            number_of_calls  +=1
                        if decision == "call":
                            number_of_calls  +=1   #need previous to be the max current bet
                            players[whos_turn].Raise(get_max_bet(players))
                            #if previous player is not the first to go all in
                            #the raise their amount
                            #need to count how many players[i].all_in = True
                            #if 1 then previous
                            #if 2 then previous previous
                            #if 3 then previous previous
                            
                      
                       
                                
            
                            #if player doesnt have enough money make them go all in
                         

                        bets = []
                        for k in range(0,nplayers):
                            bets.append(players[k].bet)
                            button("£{}/{}".format(int(players[k].bet),int(players[k].money)),
                                   nametag[k],100,
                                   130,32,
                                   black,black)
                            pygame.event.pump()
                            pygame.display.update()
                            if players[k].cards==None:
                                  button("",
                                  nametag[k],50,
                                   130,32,
                                   red,red)
                   
                        list(filter(lambda v: v != 0, bets))
                     
                        
                        button("{}".format(players[whos_turn].name),
                               nametag[whos_turn],50,
                               130,32,black,black)
                        pygame.event.pump()
                        pygame.display.update()
                        
                        #if a player is all in then we need to remove his value from the set
                        #because we use the condition that all bets need to be the same
                        #so produce a new set without all ins, but keep old one for end
          #              bets_no_all_in=[]
          #              for u in range(0,nplayers):
          #                  if players[u].all_in == True:
          #                      pass
          #                  else:
          #                      bets_no_all_in.append(players[u].bet)
          #              bets_set = set(bets_no_all_in)
                        #also when a player is all in need to append correct bet
                        #issue is probably here
                        
                        #STOP when all NONE folded none all in players have the same bet
                        #once all players have givne an input
                        print(number_of_calls)
                        if number_of_calls == nplayers - nfold:

                            flag = 0
                            break
                          
#        for i in range(0,nplayers):
#            if players[i].cards == None:
#                players[i].bet = 0
#%%  flop,turn,river              
      
        if n==0:
            money = 0
            for i in range(0,nplayers):
                money += players[i].bet
            blank.money = money
            
            
            flop.cards[0].place_on_table(table_location_card[0],2)
            flop.cards[1].place_on_table(table_location_card[1],2)
            flop.cards[2].place_on_table(table_location_card[2],2)
            b = button("pot: £{}".format(money),10,450,250,32,black,black)  
            pygame.event.pump()
            pygame.display.update()
            
        if n == 1:  
            money = 0
            for i in range(0,nplayers):
                money += players[i].bet
            flop.money = money + blank.money
           
         
            turn.cards[3].place_on_table(table_location_card[3],2)
            b = button("pot: £{}".format(money),10,450,250,32,black,black)  
            pygame.event.pump()
            pygame.display.update()
    
        if n ==2:
            money = 0
            for i in range(0,nplayers):
                money += players[i].bet
            turn.money = money + flop.money
    
            river.cards[4].place_on_table(table_location_card[4],2)
            b = button("pot: £{}".format(money),10,450,250,32,black,black)  
            pygame.event.pump()
            pygame.display.update()
        
        if n ==3:
            money = 0
            for i in range(0,nplayers):
                money += players[i].bet
            river.money = money + river.money
        
            b = button("pot: £{}".format(money),10,450,250,32,black,black)  
            pygame.event.pump()
            pygame.display.update()
            

        

        
    
    values=[]    
    for i in range(0,nplayers):
            if players[i].cards != None:
                players[i].cards[0].place_on_table(player_location_card1[i],1)
                players[i].cards[1].place_on_table(player_location_card2[i],1)
                value = winning_hand([river.cards[0], river.cards[1], river.cards[2] , river.cards[3],river.cards[4],players[i].cards[0],players[i].cards[1]])
                
            else:
                value = 0
            players[i].score = value
            values.append(value)   
          
    
    maxv = max(values)
#probably should change this and add it to the distribute_winnings()
    for i in range(0,len(values)):
        if values[i] == maxv:
            button("{}".format(players[i].name),
                   nametag[i],50,
                   130,32,red,red)
    pygame.event.pump()
    pygame.display.update()
      
#%% #distribute the money here!!!!!
    
    for player in players:
        print(player.money,player.bet)
    
    pots , players_in_pots = pot_split()
    
    #then work out who wins
    distribute_winnings(pots,players_in_pots)
    
    time.sleep(10)
    

#%% set up next round  
    display_surface.fill(white)

 
    cycle.append(cycle[0])
    cycle.pop(0)
    
   #need to remove players who are dead -> make the auto buy in

    for i in range(0,nplayers):
        if players[i].money == 0 :
            players[i].money = 1000
            players[i].buy_in +=1
            button(str(players[i].buy_in),
                   nametag[i],0,
                   32,32,
                   black,black)
            pygame.event.pump()
            pygame.display.update()
            players[i].cards = [playing_deck.deal(),playing_deck.deal()]
            
            
  


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
    
    blank.money = 0  
    flop.cards =[ playing_deck.deal(),playing_deck.deal(),playing_deck.deal()]
    flop.money = 0
    turn.cards = [flop.cards[0], flop.cards[1], flop.cards[2] , playing_deck.deal()]
    turn.money = 0
    river.cards = [turn.cards[0], turn.cards[1], turn.cards[2] , turn.cards[3], playing_deck.deal()]
    river.money = 0
    

  
    for i in range(0,nplayers):
        players[i].bet = 0
        players[i].all_in =  False
        players[i].score = 0
        players[i].fold = False
        
        
        if i < nplayers:#0,1,2
            button("£{}/{}".format(0,int(players[i].money)),
                                   nametag[i],100,
                                   130,32,
                                   black,black)
            players[i].cards = [playing_deck.deal(),playing_deck.deal()]
            pygame.event.pump()
            pygame.display.update()
            
            
            
            
      # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  

    
    
    
            
            
    
  
            


#need to account for draws and pot splitting
#if player m goes all in on pot n, they win              
            

#TODO: troubleshoot  -Fix player 1 only matters when all call
#rotate blinds
            
#one pair double counting kicker
#pair drawi
#DRAWS!!! 
#make plot splitting work
#add gui: need to produce cards for each player 
        # need to make raising work
#make it online        
    
        





    
    