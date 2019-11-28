 
import matplotlib.pyplot as plt


import plot_path
    
        
        
        
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



with open('costfull.txt') as file:
    path=[]
    n=0
    for line in file:  
       n+=1
       if n!=1:
           s=line.split(' ')
           for i in range(0,len(s)-1):
               path.append(int(s[i].rstrip()))
             


positions=[]
for i in range(0,len(path)):
  
    positions.append((path[i],int(x_index[path[i]-1]),int(y_index[path[i]-1].rstrip())))
    

#positions=sorted(positions)
print(positions)
    
indices=[]
for i in range(0,len(positions)):
    indices.append((positions[i][1],positions[i][2]))



plot_path.main(indices,'',1)
    

           
            

   
   
