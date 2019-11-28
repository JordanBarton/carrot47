

N=pow(10,7)-1
#integer between 1 and 10^7 -1

for i in range(0,N+1):
    
    if i==0:
        pass
    
    elif (i%3 ==0) & (i%5 ==0):
        
        print('FizzBuzz')
        
          
    elif i%5==0:
        
        print('Buzz')
        
    elif i%3==0:
        
        print('Fizz')
        
    else:
        
        print(i)
    
    