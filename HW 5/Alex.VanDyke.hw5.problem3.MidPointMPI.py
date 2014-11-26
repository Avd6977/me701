from mpi4py import MPI
import numpy as np 
from math import sqrt
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 20000
dims = 2
ranges = int(n/dims)

# careful---these are good only if 10000 is
# divisible by size
a = int((ranges / size)*rank)
b = int((ranges / size)*(rank+1)) - 1

dx = 1.0/float(ranges)

sums_partial = 0.0
sums = 0.0

while a <= b:
	xa = dx*a + dx/2
	a += 1
	for j in range(ranges):
		xb = dx*j + dx/2
		sums_partial += float(sqrt(xa*xb)*(dx**2))
    
if rank == 0 :
	sums += sums_partial
	for r in range(1, size) :
		sums += comm.recv(source=r, tag=123)
else :
	comm.send(sums_partial, dest=0, tag=123)
    
if rank == 0 :
	actual = 2.0**dims/3.0**dims
	err = abs(1-sums/actual)

	print "Midpoint approximation: ", sums
	print "Actual value: ", actual
	print "Relative, abs error: ", err

#mpiexec -n 4 python MPITest.py
