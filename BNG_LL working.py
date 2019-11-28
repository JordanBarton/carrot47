#convert between BNG and LL:
import numpy as np

def BNG_LL(lat2,long2):
    #given the lower left lats and longs, work out the lats and longs of a general x,y
    #x,y are the indices of grid
    #define ll_lat and ll_long to be at (0,0)
    #hence need to change in lat from (0,0)->(x,y) and then add this onto (ll_lat,l_long)
    #each step is 50m so distance from
    
    lat1 = 54.454263*np.pi/180
    long1=-3.211682*np.pi/180
    lat2=lat2*np.pi/180
    long2=long2*np.pi/180
    
    scaf_x = 655
    scaf_y = 430

    lm=0.5*(lat1+lat2)
    dla=lat1-lat2
    dlo=long1-long2
    
    k1=111.13209-0.56605*np.cos(2*lm)+0.00120*np.cos(4*lm)
    k2=111.41513*np.cos(lm)-0.09455*np.cos(3*lm)+0.00012*np.cos(5*lm)
    
    dy=k1*dla*180*1000/np.pi
    dx=k2*dlo*180*1000/np.pi
    
    di=dx/50
    dj=dy/50
    
    i=np.round(scaf_x+di)
    j=np.round(scaf_y-dj)

    return abs(999-i),j

def main(lat2,long2):
    
    i,j=BNG_LL(lat2,long2)
    
    return int(i),int(j)


    
if __name__=='main': 
    main()