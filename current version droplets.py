##############################################################################
#day 1 droplets 6/2/18 Jordan Barton
import numpy as np
import math
import matplotlib.pyplot as plt

from scipy.optimize import fsolve
from scipy.interpolate import interp1d




#==============================================================================
#function fits a polonomial of order n to a set of data
#==============================================================================
def fitting(x,y,n,yerror,inter,arg):
       
    #fit a polonomial of order n to the data  
    
    (coeffs,covr)=np.polyfit(x,y,n,cov=True)  
    
    #calculate y(x) values for fitted curve
    
    fitted_curve=[] 
    for i in range(0,len(x)):     
        
        fit=0     
        for j in range(0,n+1):  
            
            fit+=coeffs[n-j]*pow(x[i],j)  
            
        fitted_curve.append(fit)  

    #error in fitting coefficients

    for j in range(0,n+1):
        
        print(j,coeffs[j],math.sqrt(covr[j][j]))


    #chi-squared and error estimate
    
    error2=0
    for k in range (0,len(x)): 
        
        error2+=pow(y[k]-fitted_curve[k],2)/(len(x)-3)
    
    redchi2=0
    for t in range(0,len(x)-1):  
        
        redchi2+=pow(y[t]-fitted_curve[t],2)/(pow(yerror[t],2)*(len(x)-2)) 
   
    print("CHI2 reduced IS",redchi2)
    print("error estimate is",math.sqrt(error2))




    #plot data or residuals 
    if arg=='plot': 
    
        plt.errorbar(x,fitted_curve,yerror)
        
    if arg=='res': 
        
        
        speedfit=np.polyval(coeffs,x)    
        plt.errorbar(x,speedfit-y,yerr=yerror,color='k',fmt='o')
       


#==============================================================================
# read in data files
#==============================================================================

TD11= np.loadtxt('Silicon150FPS.txt')


#==============================================================================
# create arrays of all radii, mean radii and height
#==============================================================================

#drop 1 (top)
R_mean_D1=[]
x11=[]
y11=[]
z11=[]

for i in range(0,len(TD11)):
    
    #create radii array for each run, and also a mean radii array
   x11.append(TD11[i,0])
   y11.append(TD11[i,1])
   z11.append(TD11[i,2])
   

 

print(x11)

  
    
    
    
    
    
    
    

#==============================================================================
#calculate errors via mean of observed quantities
#==============================================================================
#radius error

R_error_D1=[]
R_error_D2=[]
R_error_DS=[]
for i in range (0,len(R_mean_D1)):
    
    R_error_D1.append((math.sqrt(pow(RD11[i]-R_mean_D1[i],2)+pow(RD12[i]-R_mean_D1[i],2)+pow(RD13[i]-R_mean_D1[i],2))/math.sqrt(3))/math.sqrt(2))

for i in range(0,len(R_mean_D2)):
    
    R_error_D2.append(math.sqrt(pow(RD21[i]-R_mean_D2[i],2)+pow(RD22[i]-R_mean_D2[i],2))/math.sqrt(2))

for i in range(0,len(R_mean_DS)):
    
    R_error_DS.append(math.sqrt(pow(RDS1[i]-R_mean_DS[i],2)+pow(RDS2[i]-R_mean_DS[i],2)+pow(RDS3[i]-R_mean_DS[i],2)+pow(RDS4[i]-R_mean_DS[i],2)+pow(RDS5[i]-R_mean_DS[i],2)+pow(RDS6[i]-R_mean_DS[i],2))/math.sqrt(5)/math.sqrt(6))

    
   




#-----------------------------------------------------------------------------
fitted_curve2= fitting(theta_mean_DS,speed_mean_DS,3,speed_error_DS_2,'yes','no')
#-----------------------------------------------------------------------------











