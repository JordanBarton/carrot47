#guess random number 19/09/19 16:57


import random



def test(y,guess):
    
    try:
        
        y=int(y)
        
        for i in range(0,len(guess)):
            
            if guess[i]==y:
                
                return False
        
        if (0<y<11):
    
            return True
        
        else:
            
            return False
        
        
    except ValueError:
        
        return False
        
    
    
def checknumber(y,guess):
    
    while test(y,guess)==False:
        
        y=input('please enter a valid number')
        test(y,guess)
        
    return y
        
        
        
        
    
r=random.randint(1,10)
print(r)
guess=[]
for i in range(0,3):
   
    print('you have', 3-i ,'attempts remaining')
    y=input('please guess a random number between 0 and 10 \n')

    ans=int(checknumber(y,guess))
    guess.append(ans)
    
    if r==ans: 
        print('you win')
    
        break
        
    else:
         i+=1
         
         if i==3:
             print('you lose')
             
            
    
    
    
    
    
