#salesman package
from tsp_solver.greedy import solve_tsp
import plot_path
import numpy as np
import csv



def main(cost,nearest,N,direct):
    
    
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
    
    
    
    

    path_numbers = solve_tsp( cost , endpoints = (212,213))
    
    
    
 
    with open(direct, 'w',newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(path_numbers)
    writeFile.close()

   
    
    
    path_names=[]
    path_indices=[]
    for i in range(0,len(path_numbers)):
        path_names.append(places[path_numbers[i]])
        path_indices.append((int(x_index[path_numbers[i]]),int(y_index[path_numbers[i]])))
        
    
    total=0
    for i in range(0,len(path_numbers)-1):
        
        start=path_numbers[i]
        end=path_numbers[i+1]
        total+=cost[start][end]
        
     
    

           
        
    return total/3600/24,path_numbers,path_indices

if __name__=='main':
    main()
    
    
    
    
    
    
