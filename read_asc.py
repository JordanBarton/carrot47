#read_asc
import numpy as np

def convert_to_txt(FILENAME):      
        #Cell size is 50mx50m
   
        ascii_grid = np.loadtxt(FILENAME,dtype='|S15',skiprows=5)
      
  

        N=len(ascii_grid[0])
        M=len(ascii_grid)
        
        Grid=[]
        for i in range(0,int(M)):
                row=[]
                for j in range(0,int(N)):
                    
                        try:
                            a=float(ascii_grid[i][j])
                            
                        except:
                            a=pow(10,10)
                            
                        
                        row.append(a)
              
                Grid.append(row)

        return Grid

def main(FILENAME):

    grid= convert_to_txt(FILENAME)

    return grid


if __name__ == 'main':

    main()
