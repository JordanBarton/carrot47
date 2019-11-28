#use monte carlo to calculate pi 19/09/2019 16:29
import numpy as np
import random
import matplotlib.pyplot as plt


n=10000
inside=0
for i in range(0,n):
    
    x=random.random()
    y=random.random()
    
    if np.sqrt(x**2+y**2) <=1:
        
        plt.plot(x,y,'go')
        
        inside=inside+1
        
    else:
        
        plt.plot(x,y,'ro')
        
    print( str(100*i/n) )
    
    
    
        
plt.show()
        
outside=n-inside

print(outside)
print(inside)

print(4*inside/n)