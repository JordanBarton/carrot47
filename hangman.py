#Hangman 19/09/2019 12:04

#The user needs to be able to input letter guesses.
#A limit should also be set on how many guesses they can use.
#Keep notifying the user of the remaining turns.

#keyphrase: the answer is easy



def test_for_string(y,new):
    
    try:
        
        y=float(y)
        
        return False
    
    except:
        
        for i in range(0,len(new)):
            
            if new[i]==y:
                
                print('please enter a NEW guess you idiot')
                
                return False
            
        
        return True
    
    
def test(y,new):
    
    while test_for_string(y,new)==False:
        
        
        y = input("what letter would you like to guess?\n")
    
        test_for_string(y,new)
        
    print('you guessed', y)
        
    return y

                        
           
        


def hangman(answer):
    
    
    


    new = ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']
    
    
   
    
   
    
    
    attempts=0
    
    
    
    while attempts!=10:
        
        y = input("what letter would you like to guess?\n")
    
        y=test(y,new)
        
        
        n=0
        m=0
        for i in range (0,len(answer)):
            
            if y != answer[i]:
            
            
                n=n+1
                
                if n==len(answer):
                    
                    attempts=attempts+1
                    
                    print('you have used ',attempts,'/10 attempts')
                    
                    if attempts==10:
                        
                        print('hence, you lose')
                
                
            
            if y == answer[i]:
            
                new[i]=y
                
              
                
            if new[i]!='_':
                
                m=m+1
                
                if m==len(new):
                
                    print('you win!\n')
                    attempts = 10
                
        print(new)
        
    
    
print('welcome to hangman, please guess a letter, you have 10 turns to guess the word _ _ _/_ _ _ _ _ _/_ _/_ _ _ _\n')
   
answer = ['t','h','e','a','n','s','w','e','r','i','s','e','a','s','y']

hangman(answer)


#19/09/19 16:00





    