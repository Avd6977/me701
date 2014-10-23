'''

'''

import numpy as np
from iterate import iterate
Q = 1.0
k = 1.0
dx = 0.5
a = 100.0
b = -Q*(dx**2.0)/k
c = 100.0

A = np.array([[1,0,0,0,0,0],
              [1,-2,1,0,0,0],
              [0,1,-2,1,0,0],
              [0,0,1,-2,1,0],
              [0,0,0,1,-2,1],
              [0,0,0,0,0,1]])
x = np.array([[1],[1],[1],[1],[1],[1]])
b = np.array([[a],[b],[b],[b],[b],[c]])

x_new = 2.0*x

while np.max(np.abs(x_new - x)) > 0.0001:
    x_new = iterate(A, x, b)
    x = x_new
print x_new

x = np.array([[1],[1],[1],[1],[1],[1]])

x_new = 0.0*x

D = np.diag(A)
D = D.reshape(np.size(x),1)
R = A - np.diagflat(D)

while np.max(np.abs(x_new - x)) > 0.0001:
    x_new = (b - np.dot(R, x))/D
    x = x_new
    #x_new = iterate(np.dot(D, A), x, np.dot(D, b))
print x_new