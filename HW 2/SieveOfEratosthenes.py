'''
Created on Sep 17, 2014

@author: alex
'''
# Alex Van Dyke
# Sieve of Eratosthenese
# 9/19/2014
# ME 701 HW2 Problem 2

# Call your imports
import time
import math
import numpy as np

# Set the output threshold so it doesn't give [2, 3, 5, ... 99991]
np.set_printoptions(threshold='nan')

#Define beginning time
t1 = time.time()

#Create function for printing primes
def find_primes(n):
    #Define vector n+1 length of boolean 'True'
    primes = [True] * (n+1)
    
    #Define 2 to always be output
    primes[0] = primes[1] = False
    
    #Loop through values 2 through sqrt(n)
    #sqrt(n) because it is maximum prime divisor of n. Once past this,
    # there it would already be known not to be prime
    for i in xrange(2, int(math.sqrt(n)) + 1):
        # step size for second loop is i because going by one is slow
        # going by i still accounts for every value to be hit from 2 through n
        # start at i*i to undo the sqrt to ensure we capture all primes
        
        for j in xrange(i*i, n+1, i):
            
            #Change all of the values (these are now all prime values) to be False so they are output
            primes[j] = False
            
    # return all primes from 2 to n
    return np.where(primes)[0]

# Call function
a = find_primes(100000)

# Define end time
t2 = time.time()

# Output desirables
print a
print "Time elapsed was", t2-t1


''' Used http://codereview.stackexchange.com/questions/51190/sieve-of-eratosthenes-standard-and-optimized-implementation
    as a guide to the code 
'''
    