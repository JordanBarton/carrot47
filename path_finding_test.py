#path finding
import numpy
import matplotlib.pyplot as plt
import hiking_function


import sys
import numpy as np
import random 

#we are going to have 1 input the map which will be lots of 0s and 1s
#if we visit a 1 then we have an island, unless a 1 connected to that 1
#adjacently has already been visited, ignore diagonals
#                                         10010
#e.g area=[[1,0,0],[1,1,0],[0,0,1]] =>    11001
#                                         00110
     #                                    11100
#given a map how many islands and what is the largest one?

#first i am going to loop over the rows and ignore all 0s and all visited
#if i find a 1, i am going to set visited=True
#after this, i need to find all 1s (if any) connected to this
#so take a step in all 4 quadrants, ignore 0s
#if a 1 is found set visited =True
#do this repeatedly until no more 1s are found, at which point count 1
#continue with the loop over the rows


def check_island(area,i,j):
    
    start=(0,0)
    end=(4,4)
    
    for 

            

    



n=5 ;m=5
visited=np.zeros((n,m))
area=[]
for i in range(0,n):
    D=[]
    for j in range(0,m):
        D.append(0)
     
    area.append(D)
        


#visited=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#area=[[1,0,0,1],[1,1,0,0],[0,0,1,1],[1,0,1,0]]

sys.setrecursionlimit(1000)
check_island(area,0,0)
            




 
  
    