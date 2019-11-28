
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


def check_island(area,visited,i,j):

    inew=jnew=0
    if i<0 or i>=len(area) or j<0 or j>=len(area[0]):

       return 0

   
    if visited[i][j] ==1: 

        return 1

    if  area[i][j]==0:

        return 0

    if visited[i][j] ==0 and area[i][j]==1:

        visited[i][j]=1

        for step in ([-1,0],[0,1],[1,0],[0,-1]):

       
            inew=i+step[0]
            jnew=j+step[1]
            
            check_island(area,visited,inew,jnew)

        return visited[i][j]

            


def island_problem(visited,area):

    count=0

    #loop over the row
    for i in range (0,len(area)):



        #loop over the rows
        for j in range (0,len(area[0])):

            before=visited[i][j]
            visited[i][j]=check_island(area,visited,i,j)
            after=visited[i][j]
            print(i+j)

            if before!=after:

                count+=1


    print(count)



n=20 ;m=20
visited=np.zeros((n,m))
area=[]
for i in range(0,n):
    D=[]
    for j in range(0,m):
        D.append(0)
      
    
    print(D)
    area.append(D)
        
print('\n')
print(visited)

#visited=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#area=[[1,0,0,1],[1,1,0,0],[0,0,1,1],[1,0,1,0]]

island_problem(visited,area)

