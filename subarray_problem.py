
import numpy as np
import matplotlib.pyplot as plt
import random

#first need to sort array into many 0s and 1s

#then expand out 1 at a team at each end

#examples

#A->[0,0,1,1,1]
#choose term for which element goes from 0,1
#then make sub array 1 on rhs and 1 on lhs i.e [0,1] L=2
#then expand out again 1 on rhs and 1 on lhs i.e [0,0,1,1] L=4
#then try to do again, if at end of list: stop
#nb L=odd is not possible

#B->[0,1,1] returns [0,1] so L=2

#C->[0,0,1,1] returns [0,1] then [0,0,1,1] so L=4

#D->[0,0,0,1,1,1] returns [0,1] then [0,0,1,1] then [0,0,0,1,1,1] L=6







def sub_array_length(A):


    A=sorted(A)

    L=len(A)

    


    i_change=0
    for i in range(0,len(A)):

        if A[i]==0:

            pass

        if A[i]==1:

            i_change = i

            break

   #this tells us how many zeros
    #if we have more 1s than this then this is the largest
    #if we have less ones than the number of 1s is the largest

    if i_change <= len(A)-i_change:
    
            L=i_change


    if i_change > len(A)-i_change:

        L=len(A)-i_change


 

    return L

    
    
    

    


L=[]
for i in range(0,1000):

    A=[]
    for j in range(0,100):
        A.append(random.randint(0,1))
    



    l=sub_array_length(A)
    L.append(l)

bins=np.linspace(0,50,50)
plt.hist(L,bins)
plt.show()

    


