#%% - [1] Title

#Jordan Barton 
#University of Manchester School of Physics and Astronomy
#Computational physics
#04/04/2018

#Program uses numerical methods to model simple harmonic motion (SHM)
#allowing for input from the user for initial parameters
#uses 4 numerical methods: Euler, Improved-Euler, Euler-Cromer and Verlet 
#plots phase-space, energy and displacements
#allows for damping and forced oscillations

import matplotlib.pyplot as plt
from matplotlib import pyplot
import math
import numpy as np
import cmath

#%% - [2] function that asks user for input values: initial speed v0, intital position x0, 
#                                                   mass m, damping term b, spring constant k,
#                                                   number of steps s

def Input_values():
    
    print('This program will model a simple harmonic oscillator using a range of numerical methods')
    print('The best numerical method will be used for forced oscillations')
    print('Please enter the input values for oscillations')
    print('')
    
    #create a value called decline that will decline the user input if the input is invalid
    decline = 1
    #loop until the user inputs a valid input
    while decline == 1:
    
        #try to ask the user for an input, and convert to appropriate value
        try:
    
            k=float(input('please enter a spring stiffness constant in units of N/kg'))
            
            m=float(input('please enter a mass in units of kg'))
    
            x0=float(input('please enter an initial displacement in units of m'))
    
            v0=float(input('please enter an initial velocity in units of m/s'))
    
            b=float(input('please enter a damping term'))

            s=int(input('please enter a number of steps (please enter at least 100 steps)'))
            
            ds=float(input('please enter a step size'))
            
            F0=float(input('Please enter an instantaneous force in N'))
            
            Time=float(input('Please enter a time which this force is applied in units of time period '))
            
            #only proceed if k>0 and m>0 andb>=0 and T>=0 as non negative (b=0 -> no damping)
            if k>0 and m>0 and b>=0 and s>=100 and ds>0 and Time>=0: 
                
                decline = 0
                
                if (k/m)<=pow(b/(2*m),2):
                    
                    decline = 1
                    
                    print('please enter a smaller damping term')
                
                
            else:
                
                 print('Please enter appropriate values')

        #if one of inputs is inappropriate, decline and repeat loop
        except: 
        
       
        
            print('Please enter appropriate values')

    #return values to main program
    return (k,m,x0,v0,b,s,ds,F0,Time)


#%% - [3] function that uses Euler's method to calculate position and velocity of a harmonic oscillator

def Euler(k,m,x0,v0,b,s,ds):
    
    #create empty arrays to store: position x, velocity v, accleration a
    #                              energy E and time t
    x=[]
    v=[]
    a=[]
    E=[]
    t=[]
    
    #ammend the initial values to the first elements of position and velocity arrays
    x.append(x0)
    v.append(v0)
    t.append(0)
    a.append(-(b/m)*v0-(k/m)*x0)
    E.append((1/2)*k*pow(x0,2)+(1/2)*m*pow(v0,2))
 
    #loop over number of steps and use Euler's method
    for i in range(1,s):
        #reject last term, so equal length of all arrays due to inital terms appened earlier
      

      
       
        #calculate next position
        x.append(x[i-1]+ds*v[i-1])
        
        
         
        #calculate next velocity
        v.append(v[i-1]+ds*a[i-1])
        
        
        
        #calculate acceleration
        a.append(-(b/m)*v[i-1]-(k/m)*x[i-1])
        
        
        
        
        #calculate next time
        t.append(t[i-1]+ds)
        
        
        #calculate energy
        E.append((1/2)*k*pow(x[i],2)+(1/2)*m*pow(v[i],2))
        
        
    #return the arrays to the main program
    return (x,v,a,t,E)
        

#%% - [4] function that uses the improved Euler's method to calculate position and velocity of a harmonic oscillator

def improved_Euler(k,m,x0,v0,b,s,ds):
    
     
    #create empty arrays to store: position x, velocity v, accleration a
    #                              energy E and time t
    x=[]
    v=[]
    a=[]
    E=[]
    t=[]
    
    #ammend the initial values to the first elements of position and velocity arrays
    x.append(x0)
    v.append(v0)
    t.append(0)
    E.append((1/2)*k*pow(x0,2)+(1/2)*m*pow(v0,2))
    a.append(-(b/m)*v0-(k/m)*x0)
    
    
    #loop over number of steps and use Euler's method
    for i in range(1,s):
        #reject last term, so equal length of all arrays due to inital terms appened earlier
      
  
        #calculate acceleration
        a.append(-(b/m)*v[i-1]-(k/m)*x[i-1])
        
        
        #calculate next velocity
        v.append(v[i-1]+ds*a[i-1])
       
        
        #calculate next position
        x.append(x[i-1]+ds*v[i-1]+(1/2)*pow(ds,2)*a[i-1])
        
        
        #calculate next time
        t.append(t[i-1]+ds)
        
   
        
        #calculate energy
        E.append((1/2)*k*pow(x[i-1],2)+(1/2)*m*pow(v[i-1],2))
        
  
    #return the arrays to the main program
    return (x,v,a,t,E)
        


#%% - [5] function that uses the Euler-Cromer method to calculate position and velocity of a harmonic oscillator

def Cromer(k,m,x0,v0,b,s,ds):
    

    #create empty arrays to store: position x, velocity v, accleration a
    #                              energy E and time t
    x=[]
    v=[]
    a=[]
    E=[]
    t=[]
    
    #ammend the initial values to the first elements of position and velocity arrays
    x.append(x0)
    v.append(v0)
    t.append(0)
    E.append((1/2)*k*pow(x0,2)+(1/2)*m*pow(v0,2))
        
 
    #loop over number of steps and use Cromers method
    for i in range(1,s):
        #reject last term, so equal length of all arrays due to inital terms appened earlier
      
        
        #calculate next velocity
        v.append(v[i-1]*(1-(b/m)*ds)-(k/m)*ds*x[i-1])
       
        
        #calculate next position
        x.append(x[i-1]+ds*v[i])
        
        
        #calculate next time
        t.append(t[i-1]+ds)
        
        
        #calculate energy
        E.append((1/2)*k*pow(x[i-1],2)+(1/2)*m*pow(v[i-1],2))
        
    
    #return the arrays to the main program
    return (x,v,a,t,E)


#%% - [6] function that uses the Verlet method to calculate position and velocity of a harmonic oscillator


def Verlet(k,m,x0,v0,b,s,ds):
    

    #create empty arrays to store: position x, velocity v, accleration a
    #                              energy E and time t
    x=[]
    v=[]
    a=[]
    E=[]
    t=[]
    
    #ammend the initial values to the first elements of position and velocity arrays
    x.append(x0)
    v.append(v0)
    t.append(0)
    E.append((1/2)*k*pow(x0,2)+(1/2)*m*pow(v0,2))
    
    
    
    
    #calculate parameters requared for Verlet method
    D=(b*ds)+(2*m)
    A=2*(2*m-k*pow(ds,2))/D
    B=((b*ds)-(2*m))/D    

    #calculate initial acceleration
    a0=-(b/m)*v0-(k/m)*x0
    
    #calculate the next terms of position using improved-Euler
    x.append(x0+(ds*v0)+((1/2)*pow(ds,2)*a0))
        
    
    #lose last term due to velocity, both arrays must have same length
    for i in range(2,s+1):
      #calculate next position
            x.append((A*x[i-1])+(B*x[i-2]))
        
    
    
    
    #loop over number of steps and use Cromers method
    for i in range(1,s):
        #reject last term, so equal length of all arrays due to inital terms appened earlier
     
        #calculate next velocity
        v.append((x[i+1]-x[i-1])/(2*ds))
       
        
        #calculate next time
        t.append(t[i-1]+ds)
        
        
    #append last term
    t.append(t[s-1]+ds)
        
    for i in range(1,s):
       
        
        #calculate energy
        E.append((1/2)*k*pow(x[i-1],2)+(1/2)*m*pow(v[i-1],2))
        
    
    #remove last elements of time and displacement array so all arrays equal length    
    x.pop()
    t.pop()
   
    
    
    #return the arrays to the main program
    return (x,v,a,t,E)



#%% - [7] Function that looks analytically at the solution depending on the critical damping term

def analytic(k,m,x0,v0,b,s,ds):

 #create empty arrays to store: position x, velocity v, accleration a
    #                              energy E and time t
    x=[]
    v=[]
    a=[]
    E=[]
    t=[]
    
    #ammend the initial values to the first elements of position and velocity arrays
    x.append(x0)
    v.append(v0)
    t.append(0)
    E.append((1/2)*k*pow(x0,2)+(1/2)*m*pow(v0,2))
    
   
   
    #calculate the gamma factor
    gamma=b/m
    
    

    #calculate the angular frequency squared
    w_squared=(k/m)-(pow(gamma/2,2))

    #for heavy damping
    if b>b_crit:
        
        #calculate values of D and C (physically not important)
        C=(1/(2*math.sqrt(-w_squared)))*(v0+((x0*gamma)/2))+x0/2        
        
        D=x0-C
        
        #loop over all steps
        for i in range(1,s):
        
            #append times to empty time array
            t.append(t[i-1]+ds)
        
            #append displacements to displacement array 
            x.append((C*math.exp(((math.sqrt(-w_squared)-(gamma/2))*t[i])))+ (D*math.exp((-((math.sqrt(-w_squared)+(gamma/2))*t[i])))))
        
            #append velocities to velocity array
            v.append((math.sqrt(-w_squared)-(gamma/2))*C*math.exp(((math.sqrt(-w_squared)-(gamma/2))*t[i]))+ ((-((math.sqrt(-w_squared)+(gamma/2)))*D*math.exp((-((math.sqrt(-w_squared)+(gamma/2))*t[i]))))))
        
            #append energies to energy array
            E.append(((1/2)*m*pow(v[i],2))+((1/2)*k*pow(x[i],2)))
        
      
        
        
        
    #if light dampping 
    if b<b_crit:
        
        #calculate values of A and B (physically not important)
        A=(1/(2*1j*math.sqrt(w_squared)))*(v0+((x0*gamma)/2))+(x0/2)
        
        B=x0-A
        
        #loop over all steps
        for i in range(1,s):
        
            #append times to time array
            t.append(t[i-1]+ds)
        
            #append displacements to displacement array (note use of cmath due to complex exponents)   
            x.append(A*cmath.exp((1j*math.sqrt(w_squared)-(gamma/2))*t[i])+ B*cmath.exp(-(1j*math.sqrt(w_squared)+(gamma/2))*t[i]))
          
            #append velocity to velocity array
            v.append((1j*math.sqrt(w_squared)-(gamma/2))*A*cmath.exp((1j*math.sqrt(w_squared)-(gamma/2))*t[i])-(1j*math.sqrt(w_squared)+(gamma/2))*B*cmath.exp(-(1j*math.sqrt(w_squared)+(gamma/2))*t[i]))
        
            #append energies to energy array
            E.append((((1/2)*m*pow(v[i],2))+((1/2)*k*pow(x[i],2))))
            
            
            
            
    #if critical damping
    if b==b_crit:
        
        for i in range(1,s):
            
            #append times to time array
            t.append(t[i-1]+ds)
            
            #append displacement to displacement array
            x.append( (x0+(v0+(0.5*gamma*x0))*t[i])*math.exp(-0.5*gamma*t[i]))
        
            #append velocities to velocity array
            v.append((-0.5*gamma*x0+(v0+(0.5*gamma*x0))*(1-(0.5*gamma*t[i])))*math.exp(-0.5*gamma*t[i]))
        
            #append energies to energy array
            E.append((((1/2)*m*pow(v[i],2))+((1/2)*k*pow(x[i],2))))
   
    
    #return arrays function call
    return (x,v,a,t,E)

    
#%% - [8] Function that plots graphs of displacement and energy vs time for all methods

def graphs(k,m,x0,v0,b,s,ds):
    
    print('Graphs of displacement vs time and energy vs time will now be plotted for 4 numerical models as well as the analytical solution')
    print('This is for the case of unforced oscillations')
    print('')
    
    #return x,v,a,t and E for all 5 methods    
    Eul = (Eul_x,Eul_v,Eul_a,Eul_t,Eul_E)=Euler(k,m,x0,v0,b,s,ds)

    imp_Eul = (imp_Eul_x,imp_Eul_v,imp_Eul_a,imp_Eul_t,imp_Eul_E)=improved_Euler(k,m,x0,v0,b,s,ds)

    Ver = (Ver_x,Ver_v,Ver_a,Ver_t,Ver_E)=Verlet(k,m,x0,v0,b,s,ds)

    Cro = (Cro_x,Cro_v,Cro_a,Cro_t,Cro_E)=Cromer(k,m,x0,v0,b,s,ds)

    ana = (ana_x,ana_v,ana_a,ana_t,ana_E)=analytic(k,m,x0,v0,b,s,ds)
    
    
    
    #plot figure 1 (displacement vs time)
    plt.figure(1)
    
    #add title, x label and y label for displacement vs time for all 5 methods
    plt.title('Comparing numerical methods of a simple harmonic oscillator')
    
    plt.xlabel('time/s')
    
    plt.ylabel('displacement/m')
     
    
    #plot displacement vs time for all 5 methods
    plt.plot(Eul_t,Eul_x,'b',label='Euler')
    
    plt.plot(imp_Eul_t,imp_Eul_x,'g',label='improved-Euler')
    
    plt.plot(Ver_t,Ver_x,'r',label='Verlet')

    plt.plot(Cro_t,Cro_x,'c',label='Cromer')
    
    plt.plot(ana_t,ana_x,'y',label='analytic')

    #display legend
    plt.legend()
    
    
    #plot figure 2 (energy vs time)
    plt.figure(2)
    
    #plot a log-log graph
    pyplot.yscale('log')
    
    pyplot.xscale('log')
    
    #add a title x label and y label for energy vs time for all 5 methods
    plt.title('Comparing numerical methods of a simple harmonic oscillator')
    
    
    #plot a log scale
    plt.xlabel('log(time)')
    
    plt.ylabel('log(Energy)') 
    

    #plot energy vs time for all methods
    plt.plot(Eul_t,Eul_E,'b',label='Euler')
    
    plt.plot(imp_Eul_t,imp_Eul_E,'g',label='improved-Euler')
    
    plt.plot(Ver_t,Ver_E,'r',label='Verlet')

    plt.plot(Cro_t,Cro_E,'c',label='Cromer')
    
    plt.plot(ana_t,ana_E,'y',label='analytic')

    #display legend
    plt.legend()
    
   
    #create empty displacement difference arrays
    Eul_x_diff=[]
    imp_Eul_x_diff=[]
    Cro_x_diff=[]
    Ver_x_diff=[]
    

    #loop over number of steps
    for i in range (0,len(Eul[0])):
        
       
        
        
        #on a point by point basis for each method subtract the analytical displacement and take the absolute values
        Eul_x_diff.append(abs(Eul_x[i]-np.real(ana_x[i])))
        
        imp_Eul_x_diff.append(abs(imp_Eul_x[i]-np.real(ana_x[i])))
    
        Cro_x_diff.append(abs(Cro_x[i]-np.real(ana_x[i])))
    
        Ver_x_diff.append(abs(Ver_x[i]-np.real(ana_x[i])))
    
    
    
    
    
    
    
    #plot displacement difference as a function of time for all 4 methods
    plt.figure(3)
    
    #display a title, xlabel and ylabel
    plt.title('deviation in displacement from analytic solution')
    
    plt.xlabel('time /s')
    
    plt.ylabel('deviation /m')
    
    #plot the graphs
    plt.plot(Eul_t,Eul_x_diff,'b',label='Euler')
    
    plt.plot(imp_Eul_t,imp_Eul_x_diff,'g',label='Improved-Euler')
    
    plt.plot(Ver_t,Ver_x_diff,'r',label='Verlet')
    
    plt.plot(Cro_t,Cro_x_diff,'c',label='Cromer')
    
    #display a legend
    plt.legend()
  
    
    #create empty energy difference arrays
    Eul_E_diff=[]
    imp_Eul_E_diff=[]
    Cro_E_diff=[]
    Ver_E_diff=[]
    
    #loop over all steps
    for i in range (0,len(Eul[0])):
        
        
        
        #on a point by point basis calculate the difference in energy between each solution
        #and the analytic solution and take the abosulte value
        Eul_E_diff.append(abs(Eul_E[i]-np.real(ana_E[i])))
        
        imp_Eul_E_diff.append(abs(imp_Eul_E[i]-np.real(ana_E[i])))
    
        Cro_E_diff.append(abs(Cro_E[i]-np.real(ana_E[i])))
    
        Ver_E_diff.append(abs(Ver_E[i]-np.real(ana_E[i])))
    
    
    #plot energy difference as a function of time
    plt.figure(4)
    
    #include a title, xlabel and ylabel
    plt.title('deviation in energy from analytic solution')
    
    plt.xlabel('time /s')
    
    plt.ylabel('energy /J')
    
    
    #plot the graphs
    plt.plot(Eul_t,Eul_E_diff,'b',label='Euler')
    
    plt.plot(imp_Eul_t,imp_Eul_E_diff,'g',label='Improved-Euler')
    
    plt.plot(Ver_t,Ver_E_diff,'r',label='Verlet')
    
    plt.plot(Cro_t,Cro_E_diff,'c',label='Cromer')
    
    #include a legend
    plt.legend()
  
    
    #write out data to files
    try:
        
        #write the files out to txt documents include x,v,a,t,E (no a for ana, Cro and Ver)
        Euler_file=open('Euler.txt','w')
    
        #loop over all lines
        for i in range (0,len(Eul[0])):
       
            #write out line
            Euler_file.write(str(Eul_x[i])+'\t'+str(Eul_v[i])+'\t'+str(Eul_a[i])+'\t'+str(Eul_t[i])+'\t'+str(Eul_E[i])+'\n')
      
        #close file
        Euler_file.close()
        
    except:
        
        print('Euler file could not be written')
    
    
    
    try:
    
        imp_Euler_file=open('imp_Euler.txt','w')
    
        #loop over all lines
        for i in range (0,len(imp_Eul[0])):
       
            #write out line
            imp_Euler_file.write(str(imp_Eul_x[i])+'\t'+str(imp_Eul_v[i])+'\t'+str(imp_Eul_t[i])+'\t'+str(imp_Eul_E[i])+'\n')
      
        #close file
        imp_Euler_file.close()
    
    #print failure if file could not be written
    except:
        
        print('improved Euler file could not be written')
    
    
    
    
    try:
    
            Verlet_file=open('Verlet.txt','w')
    
            #loop over all lines
            for i in range (0,len(Ver[0])):
       
                #write out line
                Verlet_file.write(str(Ver_x[i])+'\t'+str(Ver_v[i])+'\t'+str(Ver_t[i])+'\t'+str(Ver_E[i])+'\n')
      
            #close file
            Verlet_file.close()
    
    #print failure if file could not be written
    except:
        
        print('Verlet file could not be written')
    
    
    
    try:
    
    
        Cromer_file=open('Euler-Cromer.txt','w')
    
        #loop over all lines
        for i in range (0,len(Cro[0])):
       
            #write out line
            Cromer_file.write(str(Cro_x[i])+'\t'+str(Cro_v[i])+'\t'+'\t'+str(Cro_t[i])+'\t'+str(Cro_E[i])+'\n')
      
        #close file
        Cromer_file.close()
          
    #print failure if file could not be written
    except:
    
        print('Euler-Cromer file could not be written')
        
    
    try:
    
        analytic_file=open('analytic.txt','w')
    
        #loop over all lines
        for i in range (0,len(ana[0])):
       
            #write out line
            analytic_file.write(str(np.real(ana_x[i]))+'\t'+str(np.real(ana_v[i]))+'\t'+'\t'+str(np.real(ana_t[i]))+'\t'+str(np.real(ana_E[i]))+'\n')
      
        #close file
        analytic_file.close()
    
    #print failure if file could not be written
    except:
    
        print('analytic could not be written')
    
    
    #return values to function call
    return ana_t
        
#%% - [9] Function that determines the best method via the trapezoidal method
        #This is how we determine which method is best
        #smallest difference in areas = best method
        #calculate difference in areas for each method by integrating difference in energies vs time
        #use numerical trapz intgegratoin
   

def best(k,m,x0,v0,b_crit,s,ds):
    
    
    print('The best method will now be determined by considering the energy difference between analytical and numerical solutions')
    print('')
    
    
    #create empty arrays for deviation in energy between numerical and analytical solution
    #arrays for Euler, E, improved Euler, im, Euler-Cromer, C, and Verlet V
    E=[]
    im=[]
    C=[]
    V=[]
    
    #create an empty damping array
    B=[]
    
    
    for n in range(0,200):
    
        
        
            #create a damping term from 0 to 2b_crit in intervals of 0.01b_crit
            bb=n*b_crit/100
        
            #append to empty damping array
            B.append(bb/b_crit)
    
            #run each numerical model and analytical solution, though we only require the energy output
            (Eul_x,Eul_v,Eul_a,Eul_t,Eul_E)=Euler(k,m,x0,v0,bb,s,ds)

            (imp_Eul_x,imp_Eul_v,imp_Eul_a,imp_Eul_t,imp_Eul_E)=improved_Euler(k,m,x0,v0,bb,s,ds)

            (Ver_x,Ver_v,Ver_a,Ver_t,Ver_E)=Verlet(k,m,x0,v0,bb,s,ds)

            (Cro_x,Cro_v,Cro_a,Cro_t,Cro_E)=Cromer(k,m,x0,v0,bb,s,ds)

            (ana_x,ana_v,ana_a,ana_t,ana_E)=analytic(k,m,x0,v0,bb,s,ds)


            #create empty arrays for difference in energy between numerical and analytical solutions
            Eul_E_diff=[]
            imp_Eul_E_diff=[]
            Cro_E_diff=[]
            Ver_E_diff=[]

            #loop over all steps
            for i in range (0,s):
        
               
               
                   #on a point by point basis calculate the difference in energy between each solution
                   #and the analytic solution and take the abosulte value
                   Eul_E_diff.append(abs(Eul_E[i]-np.real(ana_E[i])))
           
                   imp_Eul_E_diff.append(abs(imp_Eul_E[i]-np.real(ana_E[i])))
    
                   Cro_E_diff.append(abs(Cro_E[i]-np.real(ana_E[i])))
    
                   Ver_E_diff.append(abs(Ver_E[i]-np.real(ana_E[i])))
    
        
            #work out area under 'difference in energy' curve for each numerical model
            Eul_area= np.trapz(Eul_E_diff,Eul_t,dx=ds,axis=-1)
      
            imp_Eul_area= np.trapz(imp_Eul_E_diff,imp_Eul_t,dx=ds,axis=-1)
    
            Ver_area= np.trapz(Ver_E_diff,Ver_t,dx=ds,axis=-1)
    
            Cro_area= np.trapz(Cro_E_diff,Cro_t,dx=ds,axis=-1)
    
    
            #append the area under each 'difference in energy' curve to arrays
            E.append(Eul_area)
    
            im.append(imp_Eul_area)
    
            V.append(Ver_area)
    
            C.append(Cro_area)
            
       
        
    #plot figure 15, the deviation in energy from analytical solutoin against damping
    plt.figure(15)

    #plot graphs of area under 'difference in energy' curves against damping
    plt.plot(B,E,label='Euler')
    plt.plot(B,im,label='Improved-Euler')
    plt.plot(B,V,label='Verlet')
    plt.plot(B,C,label='Euler-Cromer')


    #plot a log scale
    pyplot.yscale('log')
    pyplot.xscale('log')

    #give the figure an x-label, y-label and title
    plt.ylabel('log(deviation in area under energy curves)')
    plt.xlabel('log(b/$b_c$)')
    plt.title('Deviation in area under energy curves as a function of damping')

    #display a legend
    plt.legend()


        
        
    
#%% - [10] Function that investigates forced oscillations on the Verlet method  
    

def forced_Verlet(k,m,x0,v0,b,b_crit,s,ds,F,check,w,w0):
    
    #create empty arrays to store: position x, velocity v, accleration a
    #                              energy E and time t
    x=[]
    v=[]
    a=[]
    E=[]
    t=[]
    
    #ammend the initial values to the first elements of position and velocity and energy and time arrays
    x.append(x0)
    v.append(v0)
    t.append(0)
    E.append(((1/2)*k*pow(x0,2))+((1/2)*m*pow(v0,2)))
    
    
    
    
    #calculate parameters requared for Verlet method
    D=(b*ds)+(2*m)
    A=2*(2*m-k*pow(ds,2))/D
    B=((b*ds)-(2*m))/D    

    #calculate initial acceleration
    a0=-((b/m)*v0)-((k/m)*x0)+(F[0]/m)
    
    #calculate the next terms of position using improved-Euler
    x.append(x0+(ds*v0)+((1/2)*pow(ds,2)*a0))
        
    
    #lose last term due to velocity, both arrays must have same length
    for i in range(2,s+1):
      #calculate next position
            x.append((A*x[i-1])+(B*x[i-2])+((2*pow(ds,2)*F[i-1])))
        
    
    
    
    #loop over number of steps and use Cromers method
    for i in range(1,s):
        #reject last term, so equal length of all arrays due to inital terms appened earlier
     
        #calculate next velocity
        v.append((x[i+1]-x[i-1])/(2*ds))
       
        
        #calculate next time
        t.append(t[i-1]+ds)
        
        
    #append last term
    t.append(t[s-1]+ds)
        
    for i in range(1,s):
       
        
        #calculate energy
        E.append((1/2)*k*pow(x[i-1],2)+(1/2)*m*pow(v[i-1],2))
        
    
    #remove last elements of time and displacement array so all arrays equal length    
    x.pop()
    t.pop()
    
      #checking variable for resonance  
    if check ==3:
        
        return x
    
        
        #checking variable for unforced
    if check==0:
        
        #set fig=5 so figures 5,6,7 are plotted
        fig=5
        
        #label the damping term in terms of b_crit
        lab='b = '+str(b/b_crit)+r'$b_c$'
        
        #checking variable for instantaneously forced 
    if check==1:
        
        #set fig=8 so figures 8,9,10 plotted
        fig=8
        
        
        #label the oscillations are forced
        lab='forced'
        
    
    #checking variable for sinusoidally forced oscillations
    if check==2:
        
        #set fig=11 so figures 11,12,13 plotted
        fig=11
        
       
        lab=r'$\omega$ = '+str(w/w0)+ r'$\omega_0$'
            
        
        #checking variable for unforced oscllations on the instantaneously forced graph
    if check==4:
        
        #set fig=8 so figures 9,10,11 plotted
        fig=8
        
        #label the oscillations are unforced
        lab='unforced'
        
      
        
    #plot figure (fig) (displacement vs time)
    plt.figure(fig)
    
   
    #give the figure a title, x-label and y-label
    plt.title('Displacement of a Simple harmonic oscillator')
    
    plt.xlabel('time /s')
    
    plt.ylabel('displacement /m')
 
  
    #plot the graph
    plt.plot(t,x,label=lab)
    
    #display a legend
    plt.legend()
    
    
    
    
    #plot figure (fig+1) (energy vs time)
    plt.figure(fig+1)
    
    #give the figure a title,x-label and y-label
    plt.title('Energy variation of a Simple harmonic oscillator')
    
    plt.xlabel('time /s')
    
    plt.ylabel('Energy /J')
 
    #plot the graph
    plt.plot(t,E,label=lab)
    
    #display a legend
    plt.legend()
    
    
    #plot figure (fig+1) (phase-space)
    plt.figure(fig+2)
    
   
    #give the figure a title, x-label and y-label
    plt.title('Phase space of a Simple harmonic oscillator')
    
    plt.xlabel('displacement /m')
    
    plt.ylabel('velocity /m$s^-1$')
 
    #plot the graph
    plt.plot(x,v,label=lab)
    
    #display a legend
    plt.legend()

    
    #return the arrays to the main program
    return (x,v,a,t,E)
            

#%% - [11] Function that determines forced oscillations from user input
    
    
def forced_input(k,m,x0,v0,b,b_crit,s,ds,t,F0,T,w,w0):
    
    
    print('Using the best model, unforced, instantaneously forced and sinusoidally forced oscillations will be investigated')
    print('Graphs of displacement vs time, Energy vs time and phase-space will be plotted')
    print('')
    
    #create an empty array for unforced oscillations f_un
    F_un=[]

    #loop over all steps
    for i in range (0,s):
    
         #append 0 to every step
         F_un.append(0)


    #plot graphs of x(t) E(t) and v(x) for a range of dampings
    forced_Verlet(k,m,x0,v0,b,b_crit,s,ds,F_un,0,w,w0)

    forced_Verlet(k,m,x0,v0,b/2,b_crit,s,ds,F_un,0,w,w0)

    forced_Verlet(k,m,x0,v0,2*b,b_crit,s,ds,F_un,0,w,w0)

    forced_Verlet(k,m,x0,v0,0,b_crit,s,ds,F_un,0,w,w0)
 
    
     #convert time into step snumber
    step=round(T/ds,0)

   

    #create an empty array for instantaneously forced oscillations, F_inst
    F_inst=[]

    #loop over all steps
    for i in range (0,s):
    
        #for a given step
        if i==step:
        
            #apply a given instanenous force
            
            F_inst.append(F0)
            
        #no force is applied at other times so append 0
        else:
    
            F_inst.append(0)
        
        
        
        
    #plot graphs of x(t) E(t) and v(x) for a range of dampings
   
    forced_Verlet(k,m,x0,v0,b/8,b_crit,s,ds,F_inst,1,w,w0)

    forced_Verlet(k,m,x0,v0,b/8,b_crit,s,ds,F_un,4,w,w0)

    
    
    
    
    

    
    
    #create an empty array for sinusodially forced oscillations f_sin
    F_sin1=[]
    F_sin2=[]
    F_sin3=[]
    
    #loop over all steps
    for i in range (0,s):
    
        #append to emtpy sin array
        F_sin1.append(1*math.sin(w0*0.5*t[i]))
        F_sin2.append(1*math.sin(w0*t[i]))
        F_sin3.append(1*math.sin(w0*2*t[i]))
    
    
    
    
    
    
    #plot graphs of x(t) E(t) and v(x) for a range of dampings
    forced_Verlet(k,m,x0,v0,b/8,b_crit,s,ds,F_sin1,2,w/2,w0)

    forced_Verlet(k,m,x0,v0,b/8,b_crit,s,ds,F_sin2,2,w,w0)

    forced_Verlet(k,m,x0,v0,b/8,b_crit,s,ds,F_sin3,2,2*w,w0)

    forced_Verlet(k,m,x0,v0,b/8,b_crit,s,ds,F_un  ,2,0,w0)

    
    
#%% - [12] Function that explores resonance using the Verlet method



def resonance(k,m,x0,v0,b,b_crit,s,ds,t,w,w0):
    
    print('Resonance will now be investigated')
    print('The maximum amplitude will be plotted against driving frequency')
    print('Note, it is wise to consider a large range of times, as then the oscillator can complete a full cycle')
    print('')
   

    #create empty arrays for maximum amplitude for a range of dampings
    xmax2=[]
    xmax3=[]
    xmax4=[]
    xmax5=[]
    xmax6=[]
    omega=[]
    xmaxc=[]
    xmaxh=[]
    
    #create an empty array that shows where the peaks should occur
    peak=[]
    
    #for a range of angular frequencts from 0 to 2w0 in intervals of 0.01w0
    for j in range (0,200):
        
   

        #append the angular frequency array
        omega.append((j/100))
        
        #create empty driving force array
        F=[]
        
        #for every step
        for i in range(0,s):
        
            #for each frequency create an array for the variation of force with time
            F.append(math.sin((j/100)*w0*t[i]))
       
        
      
        #use the Verlet method for forced oscillations with a range of dampings to find displacement
        #check=3 to bypass all plots as these arent needed
        xx2=forced_Verlet(k,m,x0,v0,0.1*b,b_crit,s,ds,F,3,w,w0)
        
        xx3=forced_Verlet(k,m,x0,v0,0.2*b,b_crit,s,ds,F,3,w,w0)
        
        xx4=forced_Verlet(k,m,x0,v0,0.3*b,b_crit,s,ds,F,3,w,w0)
        
        xx5=forced_Verlet(k,m,x0,v0,0.4*b,b_crit,s,ds,F,3,w,w0)
        
        xx6=forced_Verlet(k,m,x0,v0,0.5*b,b_crit,s,ds,F,3,w,w0)
        
        xxc=forced_Verlet(k,m,x0,v0,b,b_crit,s,ds,F,3,w,w0)
        
        xxh=forced_Verlet(k,m,x0,v0,2*b,b_crit,s,ds,F,3,w,w0)
        
        #find which step is 3/4 through the displacement vs time data
        S=int(round((3*s/4),0))
      
        #remove the first 3/4 of each displacement vs time data 
        #this removes transients
        del xx2[:S]
        del xx3[:S] 
        del xx4[:S]
        del xx5[:S]     
        del xx6[:S] 
        del xxc[:S]
        del xxh[:S]
        
   
        #for each damping, of the remaining data find the maximum amplitude and append it
        xmax2.append(max(xx2))
        
        xmax3.append(max(xx3))
        
        xmax4.append(max(xx4))
            
        xmax5.append(max(xx5))
        
        xmax6.append(max(xx6))
        
        xmaxc.append(max(xxc))
        
        xmaxh.append(max(xxh))
        
    #take start of critical resonance curve as normalization constant
    amp=max(xmaxc)
    
    #create a second angular frequency array
    omega2=[]
    #from 0 to 0.1w0 in intervals of 0.001w0
    #after this is not considered as cannot square root negative numbers
    #blow up to infinity at w0
    for n in range(0,995):
        
        
        #calculate where the peak should occur
        peak.append(amp/math.sqrt(1-pow(n/1000,4)))
            
        #append the angular frequency to second frequency array 
        omega2.append(n/1000)
       
        
   #plot figure 14, the resonance curve (max amplitude vs damping)
    plt.figure(14)
   
    #plot for a range of dampings
    plt.plot(omega,xmax2,label='b = 0.1'+'$b_c$')
    
    plt.plot(omega,xmax3,label='b = 0.2'+'$b_c$')
    
    plt.plot(omega,xmax4,label='b = 0.3'+'$b_c$')
    
    plt.plot(omega,xmax5,label='b = 0.4'+'$b_c$')
    
    plt.plot(omega,xmax6,label='b = 0.5'+'$b_c$')
    
    plt.plot(omega,xmaxc,label='b = '+'$b_c$')
    
    plt.plot(omega,xmaxh,label='b = 2'+'$b_c$')
    
    plt.plot(omega2,peak,'--',label='peak')
   

    #give the graph a x-label, y-label and title
    plt.title('resonance curve for a simple harmonic oscillator')

    plt.xlabel(r'$\omega$'+'/'+r'$\omega_0$')
    
    plt.ylabel('maximum displacement /m')
    
    #remove the lower frequencies due to not enough time elapsing for max amplitude
    plt.xlim([0.25,2])
    plt.ylim([0,peak[994]])
    #display a legend
    plt.legend()

    
#%% - [13] Main code

(k,m,x0,v0,b,s,ds,F0,Time) = Input_values()


print('Time period for input damping term is ' +str(2*np.pi/(math.sqrt((k/m)-pow(b/(2*m),2))))+' s')

#calculate the resonant frequency
w0=math.sqrt(k/m)

b_crit=2*math.sqrt(k*m)

print('critical damping occurs at b =',b_crit)


#no quality factor unless damped
if b>0:
    #calculate the quality factor
    Q=(w0*m)/b

    #print the quality factor (how much energy dissapates per radian)
    print('The quality factor of the system is Q =',Q)

#plot graphs of comparison in numberical methods, return time
t=graphs(k,m,x0,v0,b,s,ds)


#let the damping term and angular frequency equal to the critical damping and resonant frequency
b=b_crit
w=w0

#calculate the time period
T=2*np.pi/(math.sqrt((k/m)-pow(b_crit/(16*m),2)))

#print the time period
print('Time period damping term '+str(b_crit/8)+' is '+str(T)+' s' )

#apply an instantaneous force at time T (in units of time period)
T=Time*T



#plot graphs of forced oscillations, x(t) E(t) and v(x)
forced_input(k,m,x0,v0,b,b_crit,s,ds,t,F0,T,w,w0)


#plot a resonance curve
resonance(k,m,x0,v0,b,b_crit,s,ds,t,w,w0)


#find the best method by the area method
best(k,m,x0,v0,b_crit,s,ds)


print('end')




#LAST DETAILS ON REPORT
    
    #WORDING
    



