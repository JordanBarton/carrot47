import csv
import BNG_xy




def read_peaks(File,direct):
    
        with open(File,'r') as file:
            places=[]
            easting=[]
            northing=[]
           
            n=0
            for line in file:
                   n+=1
                   if n!=1:
                       s=line.split(',')
                     
                      
                       if float(s[4].rstrip())==1: 
                          
                           places.append(s[0])
                           easting.append(float(s[1]))
                           northing.append(float(s[2]))
                           
        file.close()            
        return places,easting,northing               
  


def main(File,grid,direct):
    
        
    places,easting,northing = read_peaks(File,direct)
   
    x_index=[]
    y_index=[]
    
    for i in range(0,len(places)):
    
       
        n,m,h =  BNG_xy.main(easting[i],northing[i],grid)
        x_index.append(n)
        y_index.append(m)
       
        
    matrix=[]
    for i in range(0,len(places)):
        matrix.append([places[i],x_index[i],y_index[i]])
        
    
    with open(direct, 'w',newline='') as writeFile: 
        writer = csv.writer(writeFile) 
        writer.writerows(matrix)
    writeFile.close()
    
    return matrix
    


if __name__=='main':
    
    main()
    
    
   

    
    
    
    
    
    