
import numpy as np

'''
N=1
1           S=1
0,0          S=3
0,0,0         S=6
0,0,0,0       S=10

N=2
1             S=1
1/2,1/2           S=3
0,0,0         S=6
0,0,0,0       S=10

N=3
1             S=1
1,1           S=3
0,0,0         S=6
0,0,0,0       S=10


N=4
1             S=1
1,1           S=3
1/4,1/2,1/4         S=6
0,0,0,0       S=10

N=5
1          S=1
1,1           S=3
1/2,1,1/2         S=6
0,0,0,0       S=10

N=6
1           S=1
1,1           S=3
1,1,1         S=6
0,0,0,0       S=10

N=7
1            S=1
1,1           S=3
1,1,1         S=6
1/8,1/4,1/4,1/8       S=10

N=8
1            S=1
1,1           S=3
1,1,1         S=6
2/8,2/4,2/4,2/8       S=10



'''

#the number of glasses per row forms a sequence
#s=1,2,3,4,5,6
#clearly each term s_i=i where s_1 is defined to be i=0 term
#i.e we always have 1 extra item on the row than we have row themself
#the sum of the glasses will form the triangular numbers
#S=1,3,6,10
#here S_i=sum(s_j) while j<=i

#let i denote the number of rows
#let j=i+a denote the number of glasses on a row
#let N = number of glasses poured onto pyramid
#look at the case i=4 and we will try a few values of N


#want to first form the triangular numbers

s=0
S=[]
for n in range(1,10):
    
    s+=n

    S.append(s)

print(S)
N=13

for k in range(0,len(S)):
    
    if S[k]>=(N+1):

        k_change=k

        break



Nnew=N-S[k_change-1]

print(k_change)
print(Nnew)
#for N=7 need 1/8,1/4,1/4,1/8
#clearly edges = Nnew*(1/2)^k_change
A=[]

for line in range(0,k_change+1):

    A.append(0)



A[0]= A[len(A)-1]=Nnew*pow(0.5,k_change)



Nnewnew=Nnew-2*A[0]

for i in range(1,len(A)-1):

    A[i]=Nnewnew/(len(A)-1)

    

print(A)   






#so we know that we need to fill the k_change+1 th row with the remaining N

#the number of glasses poured 
