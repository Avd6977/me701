'''
Created on Sep 19, 2014

@author: alex
'''
# Alex Van Dyke
# Compute the integral of a function with Midpoint Rule, Simpson's Rule, and Gauss-Legendre Quadrature
# 9/18/2014
# ME 701 HW2 Problem 2

# Import necessary libraries (modules)
import numpy as np
from scipy.integrate import simps
import matplotlib.pyplot as plt

# Define values that will be in multiple methods


# Functions, bounds of integration, and expected answers:
# 1) f(x) = x^5, -1 to 1, 1/3
# 2) f(x) = 1/(x^2 + 1), -5 to 5, 2*atan(5)
# 3) f(x) = x*sin(x)/(1 + cos(x)^2), 0 to pi, pi^2/4

# ------------------------ First Function -----------------------
# ------------------------ Midpoint Rule ------------------------
def MidpointRule1(N, a, b):
    NList = np.arange(N) + 1
    Diff = np.ones(N)*(b-a)
    # Calculate the delta = (b-a)/N for all N
    Delta =  np.divide(Diff, NList)
    Sum = []
    for i in NList:
        Sum.append(0)
        # Create an equally space linspace for x
        x = np.linspace(a+Delta[i-1]/2, b-Delta[i-1]/2, i)
        for j in range(i):
            F = x[j]**5
            Sum[i-1] = Delta[i-1]*F + Sum[i-1]    
    return Sum
# Actual value for first problem (analytical)
Act1 = 0
midPoint1 = MidpointRule1(10, -1, 1)
# Create a relative, absolute error. Can't divide by because actual value is 0
Err1 = np.abs(np.arange(len(midPoint1))*Act1 - midPoint1)

# ------------------------ Simpson Rule ------------------------
def Simpson1(N, a, b):
    NList = np.arange(N) + 1
    Diff = np.ones(N)*(b-a)
    # Calculate the delta = (b-a)/N for all N
    Delta =  np.divide(Diff, NList)
    Sum = []
    for i in NList:
        x = np.linspace(a+Delta[i-1]/2, b-Delta[i-1]/2, i)
        y = x**5
        # Call the Simpson quadrature function
        Sum.append(simps(y,x))
    
    return Sum
        
Simps1 = Simpson1(10, -1, 1)
# Create a relative, absolute error.
Err2 = np.abs(np.arange(len(Simps1))*Act1 - Simps1)

# ------------------------ Gauss-Legendre ------------------------
def GaussLegendre1(N, a, b):
    NList = np.arange(N) + 1
    Sum = []
    for i in NList:
        Sum.append(0)
        # Create the abscisa and weights from the Gauss-Legendre polynomial method
        [x, W] = np.polynomial.legendre.leggauss(i)
        # Put the abscisa between a and b instead of -1 to 1
        x = 0.5*(b-a)*x + 0.5*(b+a)
        for j in range(i):
            F = x[j]**5
            Sum[i-1] = W[j]*F + Sum[i-1]    
        Sum[i-1] = 0.5*(b-a)*Sum[i-1]  
    return Sum    

Gauss1 = GaussLegendre1(10, -1, 1)
# Create a relative, absolute error.
Err3 = np.abs(np.arange(len(Gauss1))*Act1 - Gauss1)
        
# ------------------------ Second Function -----------------------
# ------------------------ Midpoint Rule ------------------------
def MidpointRule2(N, a, b):
    NList = np.arange(N) + 1
    Diff = np.ones(N)*(b-a)
    # Calculate the delta = (b-a)/N for all N
    Delta =  np.divide(Diff, NList)
    Sum = []
    for i in NList:
        Sum.append(0)
        x = np.linspace(a+Delta[i-1]/2, b-Delta[i-1]/2, i)
        for j in range(i):
            F = 1/(x[j]**2 + 1)
            Sum[i-1] = Delta[i-1]*F + Sum[i-1]   
    return Sum
Act2 = -2*np.arctan(0.2) + np.pi
midPoint2 = MidpointRule2(10, -5, 5)
# Create a relative, absolute error.
Err4 = np.abs(1- np.divide(midPoint2,Act2))
        
# ------------------------ Simpson Rule ------------------------
def Simpson2(N, a, b):
    NList = np.arange(N) + 1
    Diff = np.ones(N)*(b-a)
    # Calculate the delta = (b-a)/N for all N
    Delta =  np.divide(Diff, NList)
    Sum = []
    for i in NList:
        x = np.linspace(a+Delta[i-1]/2, b-Delta[i-1]/2, i)
        y = 1/(1+x**2)
        # Call the Simpson quadrature function
        Sum.append(simps(y,x))
    
    return Sum
Simps2 = Simpson2(10, -5, 5)
# Create a relative, absolute error.
Err5 = np.abs(1 - np.divide(Simps2, Act2))

# ------------------------ Gauss-Legendre ------------------------
def GaussLegendre2(N, a, b):
    NList = np.arange(N) + 1
    Sum = []
    for i in NList:
        Sum.append(0)
        # Create the abscisa and weights from the Gauss-Legendre polynomial method
        [x, W] = np.polynomial.legendre.leggauss(i)
        # Put the abscisa between a and b instead of -1 to 1
        x = 0.5*(b-a)*x + 0.5*(b+a)
        for j in range(i):
            F = 1/(1+x[j]**2)
            Sum[i-1] = W[j]*F + Sum[i-1]    
        Sum[i-1] = 0.5*(b-a)*Sum[i-1]  
    return Sum    

Gauss2 = GaussLegendre2(10, -5, 5)
# Create a relative, absolute error.
Err6 = np.abs(1 - np.divide(Gauss2, Act2))

# ------------------------ Thrid Function -----------------------
# ------------------------ Midpoint Rule ------------------------
def MidpointRule3(N, a, b):
    NList = np.arange(N) + 1
    Diff = np.ones(N)*(b-a)
    # Calculate the delta = (b-a)/N for all N
    Delta =  np.divide(Diff, NList)
    Sum = []
    for i in NList:
        Sum.append(0)
        x = np.linspace(a+Delta[i-1]/2, b-Delta[i-1]/2, i)
        for j in range(i):
            F = x[j]*np.sin(x[j])/(1 + np.cos(x[j])**2)
            Sum[i-1] = Delta[i-1]*F + Sum[i-1]
    return Sum

Act3 = np.pi**2/4
midPoint3 = MidpointRule3(10, 0, np.pi)
# Create a relative, absolute error.
Err7 = np.abs(1 - np.divide(midPoint3,Act3))

# ------------------------ Simpson Rule ------------------------
def Simpson3(N, a, b):
    NList = np.arange(N) + 1
    Diff = np.ones(N)*(b-a)
    # Calculate the delta = (b-a)/N for all N
    Delta =  np.divide(Diff, NList)
    Sum = []
    for i in NList:
        x = np.linspace(a+Delta[i-1]/2, b-Delta[i-1]/2, i)
        y = x*np.sin(x)/(1+np.cos(x)**2)
        # Call the Simpson quadrature function
        Sum.append(simps(y,x))
    
    return Sum

Simps3 = Simpson3(10, 0, np.pi)
# Create a relative, absolute error.
Err8 = np.abs(1 - np.divide(Simps3, Act3))

# ------------------------ Gauss-Legendre ------------------------
def GaussLegendre3(N, a, b):
    NList = np.arange(N) + 1
    Sum = []
    for i in NList:
        Sum.append(0)
        # Create the abscisa and weights from the Gauss-Legendre polynomial method
        [x, W] = np.polynomial.legendre.leggauss(i)
        # Put the abscisa between a and b instead of -1 to 1
        x = 0.5*(b-a)*x + 0.5*(b+a)
        for j in range(i):
            F = x[j]*np.sin(x[j])/(1+np.cos(x[j])**2)
            Sum[i-1] = W[j]*F + Sum[i-1]    
        Sum[i-1] = 0.5*(b-a)*Sum[i-1]  
    return Sum    

Gauss3 = GaussLegendre3(10, 0, np.pi)
# Create a relative, absolute error.
Err9 = np.abs(1 - np.divide(Gauss3, Act3))


# Function to graph all of the error vectors
def PrintErr(N, Err1, Err2, Err3, Err4, Err5, Err6, Err7, Err8, Err9):   
    NList = np.arange(N) + 1
    plt.figure(1)
    plt.plot(NList, Err1, 'k', NList, Err2, 'r', NList, Err3, 'g')
    plt.xlabel(NList); plt.ylabel("Relative, absolute error")
    plt.legend(["Midpoint", "Simpson", "Gauss-Legendre"])
    plt.figure(2)
    plt.plot(NList, Err4, 'k', NList, Err5, 'r', NList, Err6, 'g')
    plt.xlabel(NList); plt.ylabel("Relative, absolute error")
    plt.legend(["Midpoint", "Simpson", "Gauss-Legendre"])
    plt.figure(3)
    plt.plot(NList, Err7, 'k', NList, Err8, 'r', NList, Err9, 'g')
    plt.xlabel(NList); plt.ylabel("Relative, absolute error")
    plt.legend(["Midpoint", "Simpson", "Gauss-Legendre"])
    plt.show()
PrintErr(10, Err1, Err2, Err3, Err4, Err5, Err6, Err7, Err8, Err9)


# It was odd that the midpoint method performed so well even when compared to these other more complex methods
# The graph of the first function is also interesting, since the error is so close to zero, the precision of the 
# data is being hit so that makes the graphs jump sparatically off of zero.
