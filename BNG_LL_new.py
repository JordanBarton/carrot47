#convert between BNG and LL:
import numpy as np


def calculateDistance(long1,long2,lat1,lat2):
    
    dlo=long1-long2
    dla=lat1-lat2
    R=6371e3 #metres
    
    a=np.power(np.sin(0.5*dla),2)+np.cos(lat1)*np.cos(lat2)*np.power(np.sin(0.5*dlo),2)
    
    c=2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
    
    d=R*c
    

    return d


def method3(long1,long2,lat1,lat2):
    R=6371e3
   
    
    
    
    
    
    f=1/298.257223563
    b1=np.arctan((1-f)*np.tan(lat1))
    b2=np.arctan((1-f)*np.tan(lat2))
    
    P=(b2+b1)/2
    Q=(b2-b1)/2
    
    s=calculateDistance(long1,long2,lat1,lat2)/R
  
    
    
    x=(s-np.sin(s))*(np.sin(P)*np.cos(Q)/np.cos(s/2))**2
    
    y=(s+np.sin(s))*(np.cos(P)*np.sin(Q)/np.sin(s/2))**2
   
    print(s-f/2*(x+y))
    return R*(s-f/2*(x+y))
  
   
    
   

def main(lat2,long2):
    
    lat2=lat2*np.pi/180
    long2=long2*np.pi/180
    
    lat1 = 54.341671*np.pi/180
    long1= -3.462789*np.pi/180
    
    
    x=method3(long1,long1,lat1,lat2)
    y=method3(long1,long2,lat1,lat1)
    
    

   # x=calculateDistance(long2,long2,lat1,lat2)
        
   # y=calculateDistance(long1,long2,lat2,lat2)
   # z=calculateDistance(long1,long2,lat1,lat2)
    
   
   
    i=np.round(x/5)
    j=np.round(y/5)
    

    return int(i),int(j)
    
  

if __name__ == 'main':
    
    main()