#trapParallel_1.py
#example to run: mpiexec -n 4 python trapParallel_1.py 0.0 1.0 10000
import numpy as np
import sys
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE
from math import sqrt

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

actual = 2.0**2/3.0**2

#takes in command-line arguments [a,b,n]
a = 0.0
b = 1.0
n = 10000
ranges = n/2
dx = (b-a)/ranges

#we arbitrarily define a function to integrate
def f(x):
        return sqrt(x)

#this is the serial version of the trapezoidal rule
#parallelization occurs by dividing the range among processes
def integrateRange(a, b, n):

	integral = -(f(a) + f(b))/2.0

    # n+1 endpoints, but n trapazoids
	for i in range(ranges):
		xa = dx*i + dx/2
        for j in range(ranges):
			xb = dx*j + dx/2
			integral = integral + f(xa*xb)
	integral = integral*(dx**2)
	return integral


#h is the step size. n is the total number of trapezoids
h = (b-a)/ranges
#local_n is the number of trapezoids each process will calculate
#note that size must divide n
local_n = ranges/size

#we calculate the interval that each process handles
#local_a is the starting point and local_b is the endpoint
local_a = a + rank*local_n*h
local_b = local_a + local_n*h

#initializing variables. mpi4py requires that we pass numpy objects.
integral = np.zeros(1)
recv_buffer = np.zeros(1)

# perform local computation. Each process integrates its own interval
integral[0] = integrateRange(local_a, local_b, local_n)

# communication
# root node receives results from all processes and sums them
if rank == 0:
	total = integral[0]
	for i in range(1, size):
		comm.Recv(recv_buffer, ANY_SOURCE)
		total += recv_buffer[0]
else:
    # all other process send their result
	comm.Send(integral)

# root process prints results
if comm.rank == 0:
	err = abs(1-total/actual)
	print "Midpoint approximation: ", total
	print "Actual value: ", actual
	print "Relative, abs error: ", err
