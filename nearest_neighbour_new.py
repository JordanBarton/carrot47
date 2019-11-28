#function that determines N nearest neighbours
import copy
import csv

def nearest_neighbour(x0,y0,xi,yi,N,direct):
    
    distances=[]
    for k in range(0,len(xi)):  
        d=(int(x0)-int(xi[k]))**2+(int(y0)-int(yi[k]))**2 
        distances.append([d,k])
    new_distances=sorted(distances)
    nearest_index=[]
    nn=0
    for nn in range(0,N): 
        x=new_distances[nn]
        nearest_index.append(x[1])
    row=[]
    for j in range(0,len(xi)):
        s=0
        for i in range(0,len(nearest_index)):
                if nearest_index[i]!=j:
                    s+=1   
                if nearest_index[i]==j:
                    s+=0
        if s==len(nearest_index):
            row.append(0)
        else:
            row.append(1)            
    return row              
        
def main(N,direct):
    
   
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
    for i in range(0,len(x_index)):
        xi=copy.deepcopy(x_index)
        yi=copy.deepcopy(y_index)
        nearest_row = nearest_neighbour(xi[i],yi[i],xi,yi,N,direct)
        nearest.append(nearest_row)
        
    for i in range(0,len(nearest)):
        for j in range(0,i):
            if nearest[i][j]!=nearest[j][i]:   
                nearest[j][i]=1
                nearest[i][j]=1
                
    count=0
    for i in range (0,len(nearest)):
        for j in range(0,len(nearest)):
            if nearest[i][j]!=nearest[j][i]:
                count+=1/2
    print(count/len(nearest)**2,'nearest neighbours conflicts')

    
   
                 
    with open(direct, 'w',newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(nearest)
    writeFile.close()
    
    return nearest




if __name__ == 'main':
    
    nearest = main()
    

   
        

