#code that finds eigenvalues of a matrix and the corresponding eigenvectors
import numpy as np
from numpy import linalg as la

M = np.array([[1,0,1],[0,1,0],[1,0,1]])
print(M)

try:
    Mi=la.inv(M)  
    print(Mi)  
except la.LinAlgError:  
    pass

evalue,evector = la.eig(M)

Mt=M.T
print(Mt)

u0=evector[:,0]
u1=evector[:,1]
u2=evector[:,2]

print(evalue[0],u0)
print(evalue[1],u1)
print(evalue[2],u2)






a=np.array([1,0])
b=np.array([1,1])

print('\n')
print(np.dot(a,b))
print(np.outer(a,b))
print('\n')
print(np.hstack((a,b)))
print(np.vstack((a,b)))

