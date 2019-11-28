#wainwright
import matplotlib.pyplot as plt
import numpy as np
import re
import retrace_path
import create_maze
import path_finding_old

#use haversine distance
def calculateDistance(long1,long2,lat1,lat2):
    
    dlo=long1-long2
    dla=lat1-lat2
    R=6371e3 #metres
    
    a=np.power(np.sin(0.5*dla),2)+np.cos(lat1)*np.cos(lat2)*np.power(np.sin(0.5*dlo),2)
    
    c=2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
    
    d=R*c
    
    return d
#return distance



def read_route(File):  
    X=[]
    Y=[]
    times=[]
    
    with open(File) as file:
        n=-1
        for line in file:    #read csv and split
             n+=1
             split=line.split(',')  
             if n==0:
                 X.append('Start')
                
             else:
                 X.append(split[0])
                 
             Y.append(split[2])
             
        for i in range (0,len(Y)): 
            
            s1 = re.findall(r'[0-9]*h',Y[i]) #take hrs
            S1=pow(60,2)*float(s1[0].replace('h',''))#seconds
            
            s2 = re.findall(r'[0-9]*\:',Y[i]) #take mins
            S2=pow(60,1)*float(s2[0].replace(':',''))#seconds
            
            s3 = re.findall(r'\:[0-9]*',Y[i])#take seconds
            S3=pow(60,0)*float(s3[0].replace(':',''))#seconds
            
            S=S1+S2+S3 #sum to get seconds   
                
            times.append(S)
            
    total_distance=643302.7844925951 #metres  
    V=total_distance/np.sum(times)
   
    return V,times,X,Y


def read_peaks(File):
    
    with open(File) as file:
        
     
        places=[]
        long=[]
        lat=[]
        H=[]
        n=0
        for line in file:
               n+=1
               if n!=1:
            
                   s=line.split(',')
               
               
                   if s[9]=='1':
                       places.append(s[1])
                       lat.append(s[7])
                       long.append(s[8])
                       H.append(s[4])
                 
    return places,lat,long,H                
  


def follow_route(places,lat,long,H,times,X,V):
    
    ratio=[]
    dH=0
    
    D=[]
    height_change=[]
    for i in range (1,len(X)):
        
        actual_time=times[i]
        To=X[i]
        From=X[i-1]
     #   print(actual_time,From,To)
        
        
       
        for j in range (0,len(places)):
            
            if places[j]==To:
                
                
                for n in range(0,len(places)):
                
                    if places[n]==From:
                    
              
                        dH=float(H[n])-float(H[j])
                        
                        d=calculateDistance(np.pi/180*float(long[n]),np.pi/180*float(long[j]),np.pi/180*float(lat[n]),np.pi/180*float(lat[j]))
                        
                        height_change.append(dH)
                        
                        D.append(d)
                        
                        expected_time = d*V
                        
                        r=actual_time/expected_time
                        
                        ratio.append(r)
                        
                      
                        
    return ratio,D,height_change
                        
#%%                 
def plot_figures(ratio,height_change,D):

       
    theta=[]
    for i in range (0,len(D)):
        
        theta.append(np.arctan(height_change[i]/D[i])*180/np.pi)
            
    plt.figure(1)   
    plt.scatter(height_change,ratio)
    plt.show()
    
    plt.figure(2)
    plt.scatter(np.linspace(0,210,210),ratio)
    plt.show()
    
    plt.figure(3)
    bins=np.linspace(0,12,50)
    plt.hist(ratio,bins)
    plt.show()

    plt.figure(4)
    plt.scatter(theta,ratio)
    plt.show()
#%%                      
  
def main(grid,costs,res,friction):
    V,times,X,Y = read_route("Paul tierney route.csv")
    
    places,lat,long,H = read_peaks("coordsOfExtendedWainwrights.csv")
    
    ratio,D,height_change = follow_route(places,lat,long,H,times,X,V)
    
    expt=np.sum(times)/3600/24
    print(expt,'days from data PAUL')
    
    #plot_figures(ratio,height_change,D)
        
    places_new=[]
    for i in range(0,len(X)):
        for j in range(0,len(places)):
            if str(X[i])==str(places[j]):
               
                places_new.append(j)
                
                
   
    
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
    
   
    c=0
    maze=create_maze.main(len(grid[0]),len(grid),0)
    for i in range(0,len(places_new)-1):
        
        X=places_new[i]
        Y=places_new[i+1]
       
     
        
        
        start=(int(x_index[X].rstrip()),int(y_index[X].rstrip()))
        end=(int(x_index[Y].rstrip()),int(y_index[Y].rstrip()))
       # print(X,start,'->',Y,end)
        
        
        path = path_finding_old.main(maze,start,end)
        cost_new=retrace_path.main(path,grid,res,friction)
       # print(cost_new)
            
        c+=cost_new
        
        
        
  
    model=c/3600/24
    print(c/3600/24,' days from model PAUL')
    
    r=model/expt
    print('so our model is ',r,'times slower')
    return r

if __name__=='main':
    
    main()
    
   
            
            

        
        
        
