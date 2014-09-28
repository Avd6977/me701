'''
Created on Sep 17, 2014

@author: alex
'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

# Read in data and split into the individual columns for A, Z, and B(A,Z)
Masses = np.loadtxt('masses.txt')
Z = Masses[:,0]
A = Masses[:,1]
B = Masses[:,2]
M = len(A)

# Function to calculate the RMS and then be minimized
def Opt(a):
    # Load in the text file with all of the data
    Masses = np.loadtxt('masses.txt')
    Z = Masses[:,0]
    A = Masses[:,1]
    B = Masses[:,2]
    M = len(B)
    SumErr = 0
    for i in range(M):
        B_til = a[0]*A[i]+a[1]*A[i]**(2/3.0)+a[2]*(Z[i]**2)/(A[i]**(1/3.0))+a[3]*((A[i]-2*Z[i])**2)/(A[i])+a[4]*((-1)**(np.mod(Z[i],2)) + (-1)**(np.mod(A[i]-Z[i], 2)))/(A[i]**(1/2))
        # Calculate individual errors and square them, then add them all together
        Err = B[i] - B_til
        SqErr = Err**2
        SumErr = SumErr + SqErr
    return SumErr**0.5

# minimize the RMS by minimizing the return of the function with a0 as initial guess
a0 = [1, 0.1, 0.005, 0.02, -0.03]
out = minimize(Opt, a0)
a = out.x
# Run Opt one more time with minimized coefficients to get RMS output
RMS = Opt(a)
print "Coefficients = " + str(a)
print "av = " + str(a[0])
print "as = " + str(a[1])
print "ac = " + str(a[2])
print "aa = " + str(a[3])
print "ap = " + str(a[4])
print "RMS = " + str(RMS)


# Setup for 3D plot
B_til = np.zeros(M)
for i in range(M):
    B_til[i] = a[0]*A[i]+a[1]*A[i]**(2/3.0)+a[2]*(Z[i]**2)/(A[i]**(1/3.0))+a[3]*((A[i]-2*Z[i])**2)/(A[i])+a[4]*((-1)**(np.mod(Z[i],2)) + (-1)**(np.mod(A[i]-Z[i], 2)))/(A[i]**(1/2))

# Set figure window size
fig = plt.figure(figsize=(14,10))

# Set up the 3d axes
ax = Axes3D(fig)

# Plot a portion of B and B_til to show how close they are
ax.plot_wireframe(A[:30], Z[:30], B[:30], color='red')
ax.plot_wireframe(A[:30], Z[:30], B_til[:30])

# Set traits of the plot
ax.legend(['B','B_til'], 'upper right')
ax.set_title('Comparison of actual and least squares B values')

plt.show()
