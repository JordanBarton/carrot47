#testing path finding based on heights
import read_peaks
import read_asc
import path_finding_test
import create_maze


import matplotlib.pyplot as plt
import numpy as np


File='map.asc'

grid=np.rot90(read_asc.main(File),3)
print('grid read in')

read_peaks.main('wainwright_bng.csv',grid)
print('indices calculated')


   
with open('indices.csv') as file:
    places=[]
    x_index=[]
    y_index=[] 
    for line in file:        
       s=line.split(',')
       places.append(s[0])
       x_index.append(s[1])
       y_index.append(s[2])    
file.close()
print('indices read in')


#lets choose whitside 61 and catsye cam 134


start=(int(x_index[61].rstrip()),int(y_index[61].rstrip()))
end=(int(x_index[133].rstrip()),int(y_index[133].rstrip()))


maze = create_maze.main(len(grid[0]),len(grid),0)

path = path_finding_test.main(maze,start,end,grid)

        
for i in range(0,len(path)):
    plt.scatter(path[i][0],path[i][1])

                   
plt.show()
