import nearest_neighbour_new
import cost
import salesman_package
import read_asc
import read_peaks
import wainwright
import plot_path
import path_finding_old
import create_maze
import retrace_path


import os

import numpy as np

run_from=1
N=14
res=50
height=1
land=1


s1=r'C:\Users\username\OneDrive\python\Masters project'
s2='\\nn'+str(N)+'res'+str(res)
direct=s1+s2
try:
    os.mkdir(direct)
    print(direct)
except:
    print('directory already exists')
  



File='map'+str(res)+'.asc'
File2='fmap'+str(res)+'.asc'
grid=np.rot90(read_asc.main(File),3)
print('height data read in')

friction=np.rot90(read_asc.main(File2),3)*res
print('friction data read in')

if land!=1:
    friction=np.zeros((len(friction),len(friction)))
if height!=1:
    grid=np.zeros((len(grid),len(grid)))




direct1=r'C:\Users\username\OneDrive\python\Masters project'+'\\indices.csv'
read_peaks.main('wainwright_bng.csv',grid,direct1)
print('indices calculated')

     
direct2=direct+'\\nearest'+str(N)+'.csv'
nearest = nearest_neighbour_new.main(N,direct2)
print('nearest neighbours calculated')


direct3=direct+'\\cost'+str(N)
costs = cost.main(nearest,N,grid,direct3,run_from,res,friction)
print('costs calculated')


direct4=direct+'\\path'+str(N)+'.csv'
expt,path_numbers,path_indices=salesman_package.main(costs,nearest,N,direct4)







c=0
maze=create_maze.main(len(grid[0]),len(grid),0)
for i in range(0,len(path_numbers)-1):
    
    start=(path_indices[i][0],path_indices[i][1])
    end=(path_indices[i+1][0],path_indices[i+1][1]) 
    
    path = path_finding_old.main(maze,start,end)
    
    cost_new=retrace_path.main(path,grid,res,friction)
   
    c+=cost_new/24/60/60
    
    
    
    
print('our new record before scaling is ' ,expt)
    
print('removing euclidean the cost is ',c)

   
direct5=direct+'\\route'+str(N)+'.png'
plot_path.main(path_indices,direct5)


        
#r=wainwright.main(grid,costs,res,friction)

#new_record=c/r

#print('scaled cost is ',new_record)

#for i in range(0,len(path_numbers)):

 #   print(i,path_numbers[i],path_indices[i])




   




