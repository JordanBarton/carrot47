#create_maze
import numpy
import random


def main(N,M,prob):
    
    maze=numpy.zeros((N,M))
    for i in range(0,N):
        for j in range(0,N):
            p=random.random()
            if p<prob:         
                maze[i,j]=1 #10% likely
            else:        
                maze[i,j]=0 #90%likely
    if (int(maze[0,0]) or int(maze[N-1,N-1]))==1:
        maze[0,0]=0
        maze[N-1,N-1]=0
    
    return maze

if __name__=='main':

    main(N)
