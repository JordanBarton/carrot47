def BNG_xy(BNGx,BNGy,grid):
        
    N=len(grid)
    M=len(grid[0])
    
    ll=(300000,490000)
    ur=(350000,540000)
    
    x=(BNGx,BNGy)
    
    nx=(N*(x[0]-ll[0])/(ur[0]-ll[0]),M*(x[1]-ll[1])/(ur[1]-ll[1]))
   
    
    return int(nx[0]),int(nx[1]),grid[int(nx[0])][int(nx[1])]
    
def main(easting,northing,grid):
    
      
    i,j,h= BNG_xy(easting,northing,grid)
    
    return i,j,h
    
    
    
if __name__=='main':
    
    main()
    
    
  
            