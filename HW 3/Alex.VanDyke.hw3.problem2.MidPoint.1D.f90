program MidPoint
	implicit none
	!Variable declaration
	real :: x
	integer :: n=100, dims=1, i, ranges
	real :: dx, sums, f, actual, a, b, error

	actual = 2.0**dims/3.0**dims

	!Get lower and upper bounds from user
	print *, "Enter lower bound: "
	read *, a 
	print *, "Enter upper bound: "
	read *, b
	
	!Set the number of midpoits per dimension
	ranges = n/dims
	
	!Set dx
	dx = (b-a)/ranges

	!Calculate midpoint integral
	do i=0, ranges-1
		x = dx*i + dx/2
		f = sqrt(x)*(dx**dims)
		sums = sums + f
	end do

error = abs(1-sums/actual)
print *, "Midpoint approximation:", sums
print *, "Actual value:", actual
print *, "Relative, absolute error:", error
end program MidPoint	
