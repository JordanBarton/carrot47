#connect 4
import numpy as np
import csv

 
            
def ifwon(p,board):
    
    for i in range(0,len(board)):
        for j in range(0,len(board)):
            
            if board[i][j]==p:
            
                for n in range(-1,2):
                    for m in range(-1,2):
                        
                        try:
                     
                            if n==0 and m==0:
                                pass
                            else:
                                if board[i+1*n][j+1*m]==p:
                                    
                                    if board[i+2*n][j+2*m]==p:
                                        if board[i+3*n][j+3*m]==p:
                                            
                                            return 1
                        except: 
                            pass
            if board[i][j]==0:
                pass
    
    
        

def connect4(p,place,board):
    
    N=len(board)-1
    
    player=0
    if p==1:
        player=1
    if p==2:
        player=2
        
  
    board[0][place-1]=player   
    
    
    
    for i in range(0,N):
      
        if board[i+1][place-1]==0:
            board[i+1][place-1]=player
            board[i][place-1]=0
            
    return board
    
    
board = np.zeros((8,8))



print(board)
n=0      
playing=True
who=1
while playing==True:
    n+=1
    if n%2==0:
        who=2
        
    else:
        who=1
        
    position=int((input('where do you want to go? [1-8]')))
    
    
    while position>8 or position<1:
        print('please choose a number [1-8]')
        position=(int(input('where do you want to go? [1-8]')))
        
    while board[0][position-1]!=0 :
        print('position already taken choose somewhere else')
        position=int((input('where do you want to go? [1-8]')))
        

    
    board = connect4(who,position,board)
    print(board)


    cd =r'C:\Users\username\OneDrive\python'
    with open(cd+'\\board.csv', 'w',newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(board)
    writeFile.close()
    
    

    
    end=ifwon(1,board)
    if end ==1:
        print('player 1 wins')
        playing=False
        
    
    end=ifwon(2,board)
    if end ==1:
        print('player 2 wins')
        playing=False
    
    
   
    
        
        
        
        
        
        