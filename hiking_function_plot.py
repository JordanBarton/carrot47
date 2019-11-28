import numpy as np
import matplotlib.pyplot as plt

#returns walking velocity


#in = degrees
def tobler(theta):

    S=np.tan(theta*np.pi/180)      
    return 6*np.exp(-3.5*np.absolute(S+0.05))

def tobler_approx(theta):

    S=theta*np.pi/180
    return 6*np.exp(-3.5*np.absolute(S+0.05))


def main():
    angle=np.linspace(-50,50,500)


    velocity1=[]
    for i in range(0,len(angle)):
        velocity1.append(tobler(angle[i]))


    ratio=[]
    velocity2=[]
    for i in range(0,len(angle)):
        
        velocity2.append(tobler_approx(angle[i]))
        ratio.append(velocity2[i]/velocity1[i])





    plt.figure(1)
    plt.plot(angle,velocity1,label='toblers hiking function')
    plt.plot(angle,velocity2,label='toblers hiking function using small angle approximation')
    plt.legend()
    plt.ylabel('speed in km/hr')
    plt.xlabel('angle in degrees')
    # Show the major grid lines with dark grey lines
    plt.grid(b=True, which='major', color='#666666', linestyle='-')

    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.show()
    




    plt.figure(2)
    plt.plot(angle,ratio)
    plt.ylabel('ratio of speeds')
    plt.xlabel('angle in degrees')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')

    # Show the minor grid lines with very faint and almost transparent grey lines
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.show()
    
    plt.show()




main()


    
