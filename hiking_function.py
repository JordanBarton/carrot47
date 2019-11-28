import numpy as np

#returns walking velocity


#in = degrees
def tobler(ds,dh):

    S=dh/ds 
    
    return 6*np.exp(-3.5*np.absolute(S+0.05)) * 1000/3600


def main(x1,x2,y1,y2,h1,h2,resolution):
    
    dx=(x1-x2)*resolution #m
    dy=(y1-y2)*resolution #m
    
    ds=np.sqrt(dx**2+dy**2)
    dh=h1-h2

    v=tobler(ds,dh)
    
    
    D=np.sqrt(ds**2+dh**2)
    
    
    T=D/v
    
    return T

    

    

if __name__ == '__main__':

    
    main()
