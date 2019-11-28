#retrace path
import hiking_function
import numpy as np

def retrace_path(path,grid,res,friction):
    
    cost_path=0
    for i in range(0,len(path)-1):
     
        h1=grid[path[i][0]][path[i][1]]
        h2=grid[path[i+1][0]][path[i+1][1]]
    
        x1=path[i][0]
        x2=path[i+1][0]
        y1=path[i][1]
        y2=path[i+1][1]
    
        t_old=hiking_function.main(x1,x2,y1,y2,h1,h2,res)
        cost_path+=t_old*(friction[x2][y2]/50)
   
      

    return cost_path
            
        
        
    
 
    
def main(path,grid,res,friction):
    
    
    path_cost = retrace_path(path,grid,res,friction)
  
    return path_cost
    
    
    

if __name__ == 'main':
    main()