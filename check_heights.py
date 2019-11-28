import BNG_xy

import read_asc
import matplotlib.pyplot as plt

import numpy as np




def read_peaks(File):
    
        with open(File,'r') as file:
            places=[]
            easting=[]
            northing=[]
            height=[]
            n=0
            for line in file:
                   n+=1
                   if n!=1:
                       s=line.split(',')
                      
                       if float(s[4].rstrip())==1:
                           
                           
                           
                           places.append(s[0])
                           easting.append(float(s[1]))
                           northing.append(float(s[2]))
                           height.append(float(s[3]))
        file.close()            
        return places,easting,northing,height    






grid=np.rot90(read_asc.main('map5_new.asc'),3)
print('grid read in')


places,easting,northing,height=read_peaks('wainwright_bng.csv')

ratio=[]
for i in range(0,len(places)):

    n,m,new_height = BNG_xy.main(easting[i],northing[i],grid)
    
    print('new/old for',places[i],'is:',new_height/height[i])
    
    ratio.append(new_height/height[i])
    
    

bins=np.linspace(0.8,1.2,500)
plt.hist(ratio,bins)
plt.text(1.1,20,'mean is:'+str(np.mean(ratio)))
plt.title('ratio of heights between peak data and raster data')
plt.ylabel('frequency')
plt.xlabel('raster height/peak height')


    
    
  