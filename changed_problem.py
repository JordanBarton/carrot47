#when given an amount of money can split into £50.00 £20.00 £10.00 £5.00 £2.00
#                                    £1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01

#going to have an array called change
#will try to divide ourvalue by the first element return True or False
#then, perform the division and subtract off this amount of change
#then move onto the next term, continue subtracting change away
#stop when our value =0
import numpy as np
import matplotlib.pyplot as plt
import random

def round_down(n):


    n=n-1
    
    n_new=int(round(n))
    if n_new>n:
              return n_new

    if n_new<n:
              return n_new+1
   
    return n+1

    

def calc_change(change,value):
    N=[]
    for i in range(0,len(change)):
     
        if value/change[i] >= 1:

            
            n=round_down(value/change[i])
           
            N.append(n)

            value=value-n*change[i]
     

        else:

            N.append(0)

    
    
    return N





change=[50,20,10,5,2,1,0.50,0.20,0.10,0.05,0.02,0.01]


results=[]
for i in range(0,333):

    v=round(40*random.random())

    results.append(calc_change(change,v))


prob=[]
for i in range(0,len(change)):

    s=0
    for j in range(0,len(results)):

        s+=results[j][i]

    prob.append(s)
    



normalised_prob=(100*np.divide(prob,sum(prob)))






plt.scatter(change,normalised_prob)

    
plt.show()

    
    


    

