#3d plots 16:01 19/09/19
import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
import numpy as np

def f(x,y):
    
    return np.sin(np.sqrt(x**2+y**2))
ax=plt.axes(projection='3d')

x=np.linspace(-6,6,30)
y=x

X,Y=np.meshgrid(x,y)

Z=f(X,Y)

plt.figure(1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.contour3D(X,Y,Z,50)