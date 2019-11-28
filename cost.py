#import path_finding
#import hiking_function
import read_asc
import create_maze
#import plot_path
#import BNG_LL
import path_finding_old
#import read_peaks
#import nearest_neighbour
import retrace_path

import csv
import time




def main(nearest,N,grid,direct,run_from,res,friction):   
#%% [1] read in the block and the peak indices and nearest neighbours
    
   
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
    
    
    
#grid, places, x_index,y_index, nearest  
#use these to find nearest neighbours of a point
#%% [2] return the path by minimzing cost
    #create a maze
 
    cost=[]
    maze=create_maze.main(len(grid[0]),len(grid),0)
   
    avg=0
    for n in range(run_from-1,len(x_index)):
        start_time=float(time.time())
        
        row=[]
      
        start=(int(x_index[n]),int(y_index[n]))
        
        for i in range(0,len(x_index)):
            
            end=(int(x_index[i]),int(y_index[i]))
            
            if nearest[n][i]==1 and i!=n:
                
                path = path_finding_old.main(maze,start,end)
                
              
              
                path_cost=retrace_path.main(path,grid,res,friction)
              
                row.append(path_cost)
               
            else:  
                row.append(pow(10,10)*((start[0]-end[0])**2+(start[1]-end[1])**2))
                
           
                
       
        
        with open(direct+'_'+str(n+1)+'.csv', 'w',newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter=',')
            writer.writerow(row)
        writeFile.close()
        
       
        
        avg+=(float(time.time())-start_time)
        ETR=avg*(216-n)/(n+1)
        print(str(int(ETR)),'seconds remaining')
        
    
    for n in range(0,len(x_index)): 
        f = direct+'_'+str(n+1)+'.csv'
        with open(f) as file:
            row=[]
            for line in file:        
                s=line.split(',')
                for i in range(0,len(s)):
                    row.append(float(str(s[i])))
                cost.append(row)
        file.close()
    
    
    with open(direct+'.csv', 'w',newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter=',')
            writer.writerows(cost)
    writeFile.close()
               
               
  
    
    return cost
                
#%%   

if __name__ == 'main':
    main()
