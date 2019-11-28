'''Machine learning 09/09/2019
this is the main function
will run all functions from this one'''
import matplotlib.pyplot as plt
import numpy as np
import plot
import J

a=0.1
x=[[1,1,1,1],[2,3,4,5]]
y=[3,4,5,6]
theta=[0,0,0,0]
m=len(y)



plot.plot(x[1],y)

J.J(x,y,theta,a,m)