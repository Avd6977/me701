program MidPoint
	implicit none
	!Variable declaration
	real :: x
	integer :: n=100, dims=3, i, j, k, ranges
	real :: xa, xb, xc, xd, xe, xf, xg, xh, xi
	real :: dx, sums, f, actual, a, b, error

	actual = 2.0**dims/3.0**dims

	!Get upper and lower bounds from user
	print *, "Enter lower bound: "
	read *, a 
	print *, "Enter upper bound: "
	read *, b
	
	!Set the number of midpoits per dimension
	ranges = n/dims
	
	!Calculate dx
	dx = (b-a)/ranges

	!Midpoint rule for 3 dimensions
	do i=0, ranges-1
		xa = dx*i + dx/2
		do j=0, ranges-1
		xb = dx*j + dx/2
			do k=0, ranges-1
				xc = dx*k + dx/2
				f = sqrt(xa*xb*xc)*(dx**dims)
				sums = sums + f
			end do
		end do
	end do

error = abs(1-sums/actual)
print *, "Midpoint approximation:", sums
print *, "Actual value:", actual
print *, "Relative, absolute error:", error
end program MidPoint	
