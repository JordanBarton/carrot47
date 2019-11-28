#function that determines 5 nearest neighbours
import numpy as np
import copy
import csv

def nearest_neighbour(x0,y0,xi,yi):
    
    
   
    nn=0
    r=0
    xnn=[]
    ynn=[]
    row = np.zeros((1,len(xi)))
    while nn <6 :
        
        r+=1
        for k in range(0,len(xi)-2-nn):
            
            
            d=(int(x0)-int(xi[k]))**2+(int(y0)-int(yi[k]))**2
            
            if 0<d<r**2:
        
                xnn.append(int(xi[k]))
                ynn.append(int(yi[k]))
                xi.pop(k)
                yi.pop(k)
                
                row[0][k]=1
            
                nn+=1
                
    return row[0]
                
                
        
  
def main():
    
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
    
    
    
    nearest=[]
    for i in range(0,len(places)):
       
        xi=copy.deepcopy(x_index)
        yi=copy.deepcopy(y_index)
        
        
        nearest_row = nearest_neighbour(xi[i],yi[i],xi,yi)
       
        nearest.append(nearest_row)
        
 
    
       
    with open(r'C:\Users\username\OneDrive\python\Masters project\nearest.csv', 'w',newline='') as writeFile:
    
        writer = csv.writer(writeFile)
    
        writer.writerows(nearest)
    
    writeFile.close()


        
        
        

    
 
main()
   
        

