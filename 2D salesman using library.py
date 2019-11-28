#travelling salesman using library 
import mlrose
from tspy import TSP
import tsp
import random
import numpy as np
import math


import matplotlib.pyplot as plt


def bubble_sort(nums,X,Y):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            print('order',nums)
            print('x-coords:',X)
            print('')
            
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                X[i], X[i + 1] = X[i + 1], X[i]
                Y[i], Y[i + 1] = Y[i + 1], Y[i]
                # Set the flag to True so we'll loop again
                swapped = True
                
               
                
    return order,X,Y







def data(N):
    
    X=[]
    Y=[]
    M=np.zeros([N,N])
    for i in range(0,N):
        x=random.randint(0,10)
        y=random.randint(0,10)
        X.append(x)
        Y.append(y)
        
    for i in range(0,N):
        for j in range(0,N):
            
            M[i,j]=math.sqrt((pow(X[i]-X[j],2)+pow(Y[i]-Y[j],2)))
        
    

    return X,Y,M


def salesman(X,Y):
    
    
      
    _,order = tsp.tsp(X,Y,dist=None)
    

    
    return order


def draw(Xnew,Ynew,X,Y,order):
    

    
    
    
    fig, ax = plt.subplots()
    ax.plot(X,Y,'ro')

    for i in range(0,len(order)):
        ax.annotate(order[i], (X[i], Y[i]))

    plt.plot(Xnew,Ynew,'--')
    
    
    
        
        
N=5

X,Y,M=data(N)

order=salesman(X,Y)

order,Xnew,Ynew=bubble_sort(order,X,Y)

draw(Xnew,Ynew,X,Y,order)






