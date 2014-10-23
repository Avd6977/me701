'''
Performs the iteration for a Ax = b style problem.
For Jacobi, A = D(A)^-1*A and b = D(A)^-1*b
'''
import numpy as np

def iterate(A, x, b):
    I = np.identity(np.size(x))
    x = np.dot((I - A), x) + b 
    return(x)