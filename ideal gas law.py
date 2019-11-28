#ideal gas law 19/09/19 18:31
#ideal gas law PV=nRT with R=8.31 J/k/mol
#P>0,T>0,V>0

global R
R=8.31
global n


def test_number(x):   

    try:
        x=float(x)
        
        if x>0:
        
            return True
        
        else:
            return False
        
    except:
        
        return False
    
def test_float(x):
    
    while test_number(x)==False:
        
        x=input('please enter a valid value')
        
        test_number(x)
        
        return x
    

def test_letter(x):   

    try:
        x=str(x)
        
       
        if x == 'P':
            
            return True
        
        if x == 'V':
            
            return True
        
        if x == 'T':
            
            return True
        
        
            
        else:
            return False
          
    except:
        
        return False
    
    
def test_string(x):
    
    while test_letter(x)==False:
        
        x=input('please enter a valid letter')
        
        x=test_letter(x)
        
        return x
        
        
def ideal():
    
    x=input('what would you like to solve for, pressure (V) volume (V) or temperature (T)?\n')
    test_string(x)
    
    if x=='V':
        
        P=input('enter a value for pressure in Pascals')
        test_float(P)
        
       
        T=input('enter a value for temperature in Kelvin')
        test_float(T)

        V=n*8.31*T/P
        
        print(V)
        
    if x=='P':
        
     
        
        V=input('enter a value for volume in metres cubed')
        test_float(V)
            
        print(V)
        T=input('enter a value for temperature in Kelvin')
        test_float(T)
        
        P=n*8.31*T/V
        
    
        
    if x=='T':
        
          
        P=input('enter a value for pressure in Pascals')
        test_float(P)
        
        V=input('enter a value for volume in metres cubed')
        test_float(V)
            
     
        T=P*V/n/8.31
        
        print(T)
    
    
    
    
    
    
    
n=input('how many moles?')
test_float(n) 
print(n)


ideal()   



    
    

