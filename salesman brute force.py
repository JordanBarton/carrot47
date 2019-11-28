#travelling salesman brute force 23/09/19
import random
import matplotlib.pyplot as plt
import math
import numpy as np

def points(N): 
    X=np.zeros((N,3))
    for i in range(0,N): 
        X[i]=(random.random(),random.random(),i+1)
    return X
        
def swap(X):
    n=random.randint(0,len(X)-1)
    m=random.randint(0,len(X)-1)
    tempX=X[m][:]
    X[m][:]=X[n][:]
    X[n][:]=tempX
    print(n,m)
    return X
    
def draw(X):
    
   # fig = plt.figure(1)
  #  ax = fig.add_subplot(111)
    
    plt.plot(X,'ro')
    
  #  for i in X:
   #     
     #   ax.annotate('%s)' %j, xy=(i,j), xytext=(30,0), textcoords='offset points')
      #  ax.annotate('(%s,' %i, xy=(i,j))
    
    plt.grid()
    plt.show()
   
def dist(X):
    
    d=0
    for i in range(0,len(X)-1):
        
        
        d+=math.sqrt(pow(X[i+1][0]-X[i][0],2)+pow(X[i+1][1]-X[i][1],2))
        
    return d        
        
    
def main(N):
    
    X=points(N)

    dnew=dist(X)
    Xnew=X
    q=1
    while q==1:
    
        Xnew=swap(Xnew)
        
        d=dist(Xnew)
       
        if d<dnew:
        
            dnew=d
            
         
        elif (d-dnew)<pow(10,-8):
                
                q=0
            
        else:
            print('')
          
            
       
    #draw(Xnew)
    
    
     
            
            
       
    
N=10
main(N)
    
    
    
    

