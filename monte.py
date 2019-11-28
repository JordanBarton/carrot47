import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import linspace
from mpl_toolkits.mplot3d import Axes3D
import math
import mpl_toolkits.mplot3d
#%% - [1] Random number generator (old method that has spectral problems)
 
#  RANDSSP Multiplicative congruential uniform random number generator.
#  Based on the parameters used by IBM's Scientific Subroutine Package.
#  The statement
#     r = randssp(m,n)
#  generates an m-by-n random matrix.
#  The function can not accept any other starting seed.
#
#  This function uses the "bad" generator parameters that IBM
#  used in several libraries in the 1960's.  There is a strong
#  serial correlation between three consecutive values.

def randssp(p,q):
    

    m = pow(2, 31)
    a = pow(2, 16) + 3
    c = 0
    x = 123456789
    
    r = np.zeros([p,q])

    for l in range (0, q):
        for k in range (0, p):
         
            x = np.mod(a*x + c, m)
         
            r[k, l] = x/m
    
    
   
    return r
#%% - [2] function that generates random numbers using pythons in built function
#         Function generates random numbers x,y,z
#         plots graphs of y,x z,y,x and a histogram N,x

def pyrandom(size):
    
    x=[] #store random number x
    y=[]
    z=[]
    
    for i in range(0,size): #generate 'size' many random numbers
    
        x.append(np.random.uniform(0,1)) #generate random numbers x,y,z
       
        y.append(np.random.uniform(0,1))
       
        z.append(np.random.uniform(0,1))
        
           
    return x,y,z #return 3 arrays of random numbers of length 'size'
#%% - [3] function that generates a random unit vector

def random_unit(size):
    
    rand1=[] #create empty arrays to store 3 sets of random numbers
    rand2=[]    #the distance to the random numbers
    rand3=[]        #and the normalise random numbers
    pyth=[]
    R1=[]
    R2=[]
    R3=[]
    for i in range(0,size): #generate 'size' many random numbers
    
        rand1.append(np.random.uniform(-1,1))   #generate 3 random numbers
        
        rand2.append(np.random.uniform(-1,1))   
        
        rand3.append(np.random.uniform(-1,1))
        
        #find magnitude of random numbers
        pyth.append(math.sqrt(pow(rand1[i],2)+pow(rand2[i],2)+pow(rand3[i],2)))
        
        
        R1.append(rand1[i]/pyth[i]) #normalise random numbers
        
        R2.append(rand2[i]/pyth[i])
                
        R3.append(rand3[i]/pyth[i])
        
        
        
    return R1,R2,R3    #return 3 normalised sets of random numbers
#%% - [4] Function that generates a random exponential

def random_exp(size,lamb):
    
    e=[]    #create an empty array to store a set of random numbers
    for i in range(0,size): #generate 'size' many random numbers
        
        e.append(np.random.uniform(0,1))    #append random numbers to array
    
    x=[]#create an empty array for exponentiall distributed random numbers
    for i in range (0,size):    #for 'size' many numbers
    
        x.append(-lamb*math.log(e[i]))  #append exponential random numbers
        
    return x
#%% [5] Function that generates a random step

def random_step(size,lamb): #using the mean free path, generate a random step
    
    exp=random_exp(size,lamb)#generate a random exponentially distributed
                             #set of random numbers
    rand_unit=random_unit(size)#generate a random set of unit vectors

    step1=[]
    step2=[]
    step3=[]#empty arrays to store 3 unit vectors
    for i in range(0,size):
      
        step1.append(exp[i]*rand_unit[0][i])#generate a step in 3 directions
        step2.append(exp[i]*rand_unit[1][i])
        step3.append(exp[i]*rand_unit[2][i])
    
    return step1, step2, step3
#%% [6] Function that performs a random walk 

def random_walk(lamb,p_a,thickness):

    i=0 #count the number of steps by setting the initial step number to 0
    
    step_x=[]#create empty arrays to store the steps in 3 directions 
    step_y=[]#and the histories of the particle
    step_z=[]
    data=[]

    q=True#create a while loop using q=True or False to break the loop
    while q==True:

        i=i+1 #conut the number of steps
        
        rand=np.random.uniform(0,1)#generate a random number (probability)

        data.append(0)
      
        
        
        if rand<p_a:#if the random number is less than the probability of absorption
            
            absorb=1#the neutron has been absorbed, append this to the histories
            data.append(absorb)
            q=False#break the loop
            
            

        if rand>=p_a:#if the generated random number is greater than 
                     #or equal to the probability of absorption
             
                #generate random steps
                step_x1= random_exp(1,lamb)
                step_y1= random_exp(1,lamb)
                step_z1= random_exp(1,lamb)
                step_x2,step_y2,step_z2 = random_unit(1)
                s_vector_x = step_x1[0]*step_x2[0]
                s_vector_y = step_y1[0]*step_y2[0]
                s_vector_z = step_z1[0]*step_z2[0]
                
                if i==1: #for an incident neutron
                     
                     s_vector_y=0
                     s_vector_z=0#make sure no steps can be taken in y or z
                     
                step_x.append(s_vector_x)
                step_y.append(s_vector_y)
                step_z.append(s_vector_z)
                
                #if the total distance travelled is negative
                if np.sum(step_x)<0:
                    escape=2#the particle has been reflected
                    data.append(escape)#append this to the history array
                    q=False#break the loop
                    
                #if the total distance travelled exceeds the thickness
                if np.sum(step_x)>=thickness:
                
                    transmit=3#the particle has been transmitted
                    data.append(transmit)#append this to the history array
                    q=False#break the loop

    #return the total distance travelled, individual steps and history 
    return np.sum(step_x), np.sum(step_y), np.sum(step_z),data,step_x,step_y,step_z
#%% -[7] Function that plots a random walk 

def plot_random_walk(lamb,p_a,thickness,fig):
    
    h=True#create a while loop using h=True or False to break the loop
    while h==True:
      
        #perform a random walk 
        X,Y,Z,data,x,y,z = random_walk(lamb,p_a,thickness)
     
        #if there are more than 10 steps (so instant reflections are eliminated)
        if len(x)>10:

            h=False #break the loop

    sum_x=[]#create a collective step array
    sum_y=[]
    sum_z=[]
    
    sx=0
    sy=0
    sz=0#inital step is zero in all 3 dimensions
    for i in range(0,len(x)):
        
        sx=sx+x[i]  #for all 3 dimensions work out the collective step
        sum_x.append(sx)#add ecah step onto the previous steps
    
        sy=sy+y[i]
        sum_y.append(sy)
    
        sz=sz+z[i]
        sum_z.append(sz)
        
    #plot figure 'fig' in 3 dimensinos
    figure = plt.figure(fig)
    figure.subplots_adjust(bottom=0.25, top=0.75)
    axes = figure.gca(projection='3d')
    xLabel = axes.set_xlabel('x /cm')#x label
    yLabel = axes.set_ylabel('y /cm')#y label
    zLabel = axes.set_zlabel('z /cm')#z label


    startx=[]#empty array for the start of walk in x direction
    endx=[]#empty array for the end of walk in x direction
    startx.append(sum_x[0])#append first step in x
    endx.append(sum_x[len(sum_x)-1])#append last step in x

    starty=[]#empty array for the start of walk in y direction
    endy=[]#empty array for the end of walk in y direction
    starty.append(sum_y[0])#append first step in y
    endy.append(sum_y[len(sum_y)-1])#append last step in y

    startz=[]#empty array for the start of walk in z direction
    endz=[]#empty array for the end of walk in z direction
    startz.append(sum_z[0])#append first step in z
    endz.append(sum_z[len(sum_z)-1])#append last step in z

    #on the same axes as earlier, plot the starts and end using a green
    #and a red dot to denote start and end points
    plot = axes.plot(sum_x,sum_y,sum_z,'-')
    plot= axes.plot(endx,endy,endz,'.r')
    plot= axes.plot(startx,starty,startz,'.g')
    plt.show()
#%% [8] Function that calculates the mean depth of penetration

def depth(lamb,p_a,thickness,neutrons,fig,cancel):
    
    
    a=0#the inital absorptions,reflections,transmissions and steps is 0
    t=0
    r=0
    number=0
    d=[] #create empty arrays for distance travelled and number of steps
    scattering_events=[]#number of steps
    
    while number!=neutrons:#while the loop hasn't reached a number of neutrons
                            #that is specified by the user
      
        #perform a random walk
        net_x,net_y,net_z,data,x,y,z=random_walk(lamb,p_a,thickness)
        
        #if transmitted, count 1 onto t
        if net_x>=thickness:
            
            t=t+1
            
        #if reflected, count 1 onto r
        if net_x<0:
            
            r=r+1
            
        #if absorbed, count 1 onto a
        if 0<=net_x<thickness:
            
            a=a+1
            
            #append the depth at which absorption occurs
            d.append(net_x)
            #append the number of steps to number of steps array
            scattering_events.append(len(data))
            
        #count the number of neutrons
        number=number+1
        
    m=0#set attenuation length to 0 for when negation occurs
       
    #use a variable cancel so this can be negated
    if cancel!='cancel':
        
        #plot a histogram of depths
        plt.figure(fig)
        plt.xlabel('depth /cm')#xlabel
        plt.ylabel('frequency')#ylabel
        #return the frequency and bins
        frequency, bins,_ = plt.hist(d,100)
    
       #create arrays where we have removed the 0 terms
        new_bins = []
        log_frequency=[]
        for i in range(0,len(frequency)):
            
            if frequency[i] != 0:#if no 0 occurs
                
                new_bins.append(bins[i])#append the bins and frequency
  
                log_frequency.append(np.log(frequency[i]))

        #Least squares fit the data
        coeffs,covr = np.polyfit(new_bins,log_frequency,1,cov=True)
        
        bestfitline = []#create line of best fit
        for i in range (0,len(log_frequency)):
            
            #append best fit line using gradient and y-intercept
            bestfitline.append(coeffs[0]*new_bins[i]+coeffs[1])
          
        attenuation=-1/coeffs[0]
        frac_error=math.sqrt(covr[0][0])/coeffs[0]
     
      
        plt.figure(fig+1)
        plt.ylabel('log(N)')
        plt.xlabel('depth /cm')
        plt.scatter(new_bins,log_frequency)  
        plt.plot(new_bins,bestfitline)
        plt.show()
    
        print('attenuation length is '+ str(attenuation)+' += ' +str(frac_error*attenuation) +'/cm')
        
    #return depth, absorptions, reflections, transmissions, steps and attenuation length
    return d,a,r,t,scattering_events , m


#%% [9] Function that investigates the effect of varying thickness on a random walk

def thick_depend(lamb,p_a,upper,increment,runs,neutrons,fig):
    
    #create empty arrays to store the thickness, mean number of transmissions
    #mean number of absorptions and mean number of reflections
    thick=[]
    transmit_mean=[]
    absorb_mean=[]
    reflect_mean=[]
    
    #create empty arrays to store errors
    error_absorb=[]
    error_reflect=[]
    error_transmit=[]
    for T in range(0,upper):#for a range of thicknesses
        
        transmit=[]#create empty arrays for transmssions, reflections and absorptions
        absorb=[]
        reflect=[]
      
        for i in range(0,runs):#for 'runs' many runs
         
            #use the depth function, but do not plot figures
            _,a,r,t,_,m = depth(lamb,p_a,T*increment,neutrons,fig,'cancel')
            
            #append the number tranmissions,reflects and absorptions
            transmit.append(t)

            absorb.append(a)
        
            reflect.append(r)
            
        #use np.std on the arrays to determine the error
        error_absorb.append(np.std(absorb))
        error_reflect.append(np.std(reflect))
        error_transmit.append(np.std(transmit))
          
        #append the means to the mean arrays
        transmit_mean.append(np.mean(transmit))
        absorb_mean.append(np.mean(absorb))
        reflect_mean.append(np.mean(reflect))
        #append the thickness to the thickness array
        thick.append(T*increment)

   # ynewexp=[]
   # for i in range (0,len(thick)):

       # ynewexp.append(np.exp(m*thick[i]))

    #plot a figure, plot the tranmssions reflection and absorptions
    #as a function of thickness, with their respective errors
    plt.figure(fig)
    plt.ylabel('Fraction /%') #ylabel
    plt.xlabel('thicknesscm') #xlabel
    plt.errorbar(thick,transmit_mean,yerr=error_transmit,fmt='.r')
    
    plt.errorbar(thick,absorb_mean,yerr=error_absorb,fmt='.g')
    
    plt.errorbar(thick,reflect_mean,yerr=error_reflect,fmt='.b')
    plt.show()


    
  #  plt.errorbar(thick,ynewexp,yerr=error_t,fmt='-')
#%% [11] Function that investigates effect of number of neutrons on errors

def error_neutrons(lamb,p_a,thickness,fig):
    
    #perform 20 runs
    runs=20
    
    #create arrays for number of neutrons, percentage error of absorptions
    #reflections and transmissions
    neutrons=[]
    error_absorb=[]
    error_reflect=[]
    error_transmit=[]
    for j in range(1,12):#for 1000 to 12000 neutrons
  
        N=1000*j
        neutrons.append(N)#append number of neutrons
        
        #create empty absorption, reflection and transmission arrays
        absorb=[]
        reflect=[]
        transmit=[]
        for i in range(0,runs):#for however many runs they are
            
            #find the absorption
            _,a,r,t,_,_= depth(lamb,p_a,thickness,N,fig,'cancel')

            absorb.append(a)
            
            reflect.append(r)
    
            transmit.append(t)
    
            
            
        #append the percentage error in absorption,reflection and transmission
        error_absorb.append(100*np.std(absorb)/np.mean(absorb))
        
        error_reflect.append(100*np.std(reflect)/np.mean(reflect))
        
        error_transmit.append(100*np.std(transmit)/np.mean(transmit))
        
    #plot a figure showing the effect of Number of neutrons
    plt.figure(fig)
    plt.plot(neutrons,error_absorb,'ro',label='absorb')
    plt.plot(neutrons,error_reflect,'bo',label='reflect')
    plt.plot(neutrons,error_transmit,'go',label='transmit')
    plt.xlabel('Number of neutrons')#x label
    plt.ylabel('Percentage error /%')#y label
    plt.legend() 
#%% [12] Function that works out errors on absorption, reflection and transmission
        #and the mean values for an amount of runs

def error_absorb(lamb,p_a,thickness,N,runs):
    #empty array for absorptions, reflections and transmissions as well as
    #number of steps
    A=[]
    R=[]
    T=[]
    N=[]
    for i in range (0,runs):#perform 'runs' many runs
        
        #call depth
        D,a,r,t,scattering_events,m= depth(lamb,p_a,thickness,N,0,'cancel')
    
        #append absorptions,reflections,transmissions,number of steps
        A.append(a)
        R.append(r)
        T.append(t)
        N.append(len(scattering_events))

    #work out the errors using np.std
    error_A=np.std(A)
    error_R=np.std(R)
    error_T=np.std(T)
    error_N=np.std(N)

    print('the average number of scattering events is: ' +' '+ str(np.mean(scattering_events)))
    print('transmission is: ' + str(100*np.mean(T)/(np.mean(A)+np.mean(R)+np.mean(T)))+' '+str(100*error_T/(np.mean(A)+np.mean(R)+np.mean(T))))
    print('reflection is: ' + str(100*np.mean(R)/(np.mean(A)+np.mean(R)+np.mean(T)))+' '+str(100*error_R/(np.mean(A)+np.mean(R)+np.mean(T))))
    print('absorption is: ' + str(100*np.mean(A)/(np.mean(A)+np.mean(R)+np.mean(T)))+' '+str(100*error_A/(np.mean(A)+np.mean(R)+np.mean(T))))
    print('number of steps: ' + str(N)+' '+str(error_N)) 
#%% [13] Function that runs the random number geneation code


def user_interface_random():
    
    #introduction
    print('This program will perform two things:\n')
    print('1. The investigation of random numbers\n')
    print('2. A monte carlo simulation involving the random walks of neutrons\n')
    
    #while loop
    a=True
    while a==True:
        
        #ask for number of random numbers
       size = int(input('How many random numbers would you like to generate? (in units of 100)\n'))
    
        #if greater than 100 
       if size>0:
           
           a=False#break the loop
           
       
       size=size*100
        
    #generate 'size' many random numbers (in 3d) using LGC METHOD
    r=randssp(3,size)
    
    figure = plt.figure(1)
    #plot the random numbers
    figure.subplots_adjust(bottom=0.25, top=0.75)
    axes = figure.gca(projection='3d')
    xLabel = axes.set_xlabel('x')#x label
    yLabel = axes.set_ylabel('y')#y label
    zLabel = axes.set_zlabel('z')#z label
    plot = axes.plot(r[0,:], r[1,:], r[2,:],'.b')
    plt.show()
    
    
    
    
    
    #generate 'size' many random numbers (in 3d) using python random numbers
    x,y,z = pyrandom(size)
    
    #plot the random numbers
    figure = plt.figure(3)
    figure.subplots_adjust(bottom=0.25, top=0.75)
    axes = figure.gca(projection='3d')
    xLabel = axes.set_xlabel('x')#x label
    yLabel = axes.set_ylabel('y')#y label
    zLabel = axes.set_zlabel('z')#z label
    plot = axes.plot(x,y,z,'.b')
    
        
    
    #plot a histogram of random numbers (in 1d)
    plt.figure(4)
    plt.hist(x,100)
    plt.xlabel('x') #x label
    plt.ylabel('frequency')#y label
    plt.show()
    
    
    
    
    
    #plot 2d random numbers
    figure = plt.figure(5)
    plt.plot(x,y,'.b')
    plt.ylabel('y') #x label
    plt.xlabel('x') #y label
    plt.show()
    
    
    
    
    #generate random unit vectors of length 'size'
    x,y,z = random_unit(size)
    
    #plot unit vectors in 3d
    figure = plt.figure(7)
    figure.subplots_adjust(bottom=0.25, top=0.75)
    axes = figure.gca(projection='3d')
    xLabel = axes.set_xlabel('x') #xlabel
    yLabel = axes.set_ylabel('y') #ylabel
    zLabel = axes.set_zlabel('z') #zlabel
    plot = axes.plot(x,y,z,'.b')
    plt.show()
    
    
    
    
    #generate random steps in 3d
    unit1,unit2,unit3 = random_step(size,0.1)
    
    #plot random steps in 3d
    figure = plt.figure(9)
    figure.subplots_adjust(bottom=0.25, top=0.75)
    axes = figure.gca(projection='3d')
    xLabel = axes.set_xlabel('x')#x label
    yLabel = axes.set_ylabel('y')#y label
    zLabel = axes.set_zlabel('z')#z label
    plot = axes.plot(unit1,unit2,unit3,'.')
    plt.show()
    
    
    
    

#%% - [14] Investigates random walks

def user_interface_walk():
    
    #ask the user which material to investigate
    print('which material would you like to investigate?\n')
    
    #use a while loop to make sure the user answers
    a=True
    while a==True:
    
        material= int(input('for water type 1, lead type 2, graphite type 3\n'))
        
        if material ==1 or material==2 or material==3:
            
            a=False
    
    #water
    if material ==1:
    
        #using area and scattering cross section, as well as mass density
        sigma_A=0.6652              *1e-24         #barn->cm^2
        sigma_S=103                 *1e-24
        mass_density=1              *1e-3           #g/cm^3->kg/cm^3
        
        #calculate number density
        number_density=mass_density/(18*1.67e-27)  #u->kg
        
        #calculate probability of absorption
        p_a=sigma_A/(sigma_A+sigma_S)
        
        #calculate mean free path
        lamb=1/((sigma_A+sigma_S)*number_density)
        
        #print the mean free path
        print('WATER: mean free path is '+'probability of absorption is '+str(lamb)+str(100*p_a) +'%\n')
    
    #lead
    if material ==2:
    

        #do the maths
        sigma_A=0.158                 *1e-24         #barn->cm^2
        sigma_S=11.221                *1e-24
        
        mass_density=11.35             *1e-3           #g/cm^3->kg/cm^3
        
        number_density=mass_density/(207.2*1.67e-27)  #u->kg
        
        p_a=sigma_A/(sigma_A+sigma_S)
        
        lamb=1/((sigma_A+sigma_S)*number_density)
        
        print('LEAD: mean free path is '+str(lamb)+'probability of absorption is '+str(100*p_a) +'%\n')
    
    
    #graphite
    if material ==3:
    
        #do the maths
        sigma_A=0.0045               *1e-24         #barn->cm^2
        sigma_S=4.74                 *1e-24
        
        mass_density=1.67            *1e-3           #g/cm^3->kg/cm^3
        
        number_density=mass_density/(12*1.67e-27)  #u->kg
        
        p_a=sigma_A/(sigma_A+sigma_S)
        
        lamb=1/((sigma_A+sigma_S)*number_density)
        
        print('GRAPHITE: mean free path is '+str(lamb)+'probability of absorption is '+str(100*p_a) +'%\n')
    
    
    #ask the user the feature they would like to investigate
    print('which feature would you like to investigate?\n')
    
    #user a while loop to make sure the user choses a feature
    b=True
    while b==True:
    
        feature=int(input('for a random walk type 1, number of absorptions vs depth type 2, for the dependence of thickness on the random walk type 3, and for the error associated with number of neutrons type 4, for absorptions reflections and transmissions type 5.\n'))
    
        if feature ==1 or feature==2 or feature==3 or feature ==4 or feature==5:
            
            b=False
    
    
    #for a random walk
    if feature ==1:
    
        #use a while loop to make sure the user specifices a thickness
        c=True
        while c==True:
            
            thickness=float(input('what thickness of material would you like to use? (in units of cm)\n'))
        
            if thickness >0:
                
                c=False
        
        #plot a random walk
        plot_random_walk(lamb,p_a,thickness,100)
    
    
    #for depth of absorption
    if feature ==2:
    
        #use a while loop to make sure the user specifices a thickness and number of neutrons
        d=True
        while d==True:
            
            thickness=float(input('what thickness of material would you like to use? (in units of cm)\n'))
            neutrons=float(input('how many neutrons would you like to model? (in units of 100)\n'))
           
            if thickness >0 and neutrons>0:
               
                d=False
        
        #run the depth function
        depth(lamb,p_a,thickness,100*neutrons,200,'')
        
        
    #for thickness dependence
    if feature ==3:

        #use a while loop to make sure the user specifices number of increments,
        #increment size, number of runs and number of neutrons
        e=True
        while e==True:
            
            upper=int(input('how many times would you like to increment the thickness?\n'))
            increment=float(input('what size increment would you like to make? (in units of cm)\n'))
            runs=int(input('how many runs would you like to perform (used in determining uncertainties)\n'))
            neutrons=float(input('how many neutrons would you like to model? (in units of 100)\n'))
            
            if upper >0 and neutrons>0 and increment>0 and runs>0:
                
                e=False
                   
        #investigate thickness dependence
        thick_depend(lamb,p_a,upper,increment,runs,100*neutrons,300)
        
    #error on neutron numbers 
    if feature ==4:
        
        #use a while loop to make sure the user specifices a thickness
        f=True
        while f==True:
            
            thickness=float(input('what thickness of material would you like to use? (in units of cm)\n'))
        
            if thickness>0:
                
                f=False
        
        #investigate error in neutron numbers
        error_neutrons(lamb,p_a,thickness,400)
        
    #error on reflections, absorptions and transmissions
    if feature ==5:
        
        #use a while loop to make sure the user specifices a thickness,
        #number of neutrons and number of runs
        g=True
        while g==True:
            
            thickness=float(input('what thickness of material would you like to use? (in units of cm)\n'))
            neutrons=float(input('how many neutrons would you like to model? (in units of 100)\n'))
            runs=int(input('how many runs would you like to perform (used in determining uncertainties)\n'))
            
            if thickness >0 and neutrons>0 and runs>0:
                
                g=False
        
        #investigate error in neutron numbers
        error_absorb(lamb,p_a,thickness,100*neutrons,runs)




def main():
            
    #%% [15] MAIN function

    #do the first part of the project
    user_interface_random()

    #do the second part of the project
    user_interface_walk()

main()
    

