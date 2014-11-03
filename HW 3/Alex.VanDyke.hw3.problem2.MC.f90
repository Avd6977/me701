program MC
	implicit none
	!Variable declaration
	real :: x
	integer :: n, d, dims = 10, i, j, t1 = 0, t2 = 0, clock_rate, clock_max, time = 0
	double precision :: f, xa, sums, midpoint, actual, a, b, error

	CALL system_clock(t1, clock_rate, clock_max)	
	actual = 2**dims/3.0**dims
	
	!Get lower and upper bounds from the user
	print *, "Enter lower bound: "
	read *, a
	print *, "Enter upper bound: "
	read *, b

	!Begin random number generation
	call RANDOM_SEED()

	!Number of histories, then loop through those histories
	n = 1000000000
	do i=1, n
		xa = 1.0

		!Calculate x1*x2*...*xn for n dimensions, where xi is random
		do j=1, dims
			call RANDOM_NUMBER(x)
			xa = xa * x
		end do

		!Perform MC Quadrature on the function
		f = sqrt(xa)
		sums = sums + f/n
		end do
	error = abs(1 - sums/actual)
	CALL system_clock(t2, clock_rate, clock_max)
	time = t2 - t1
	
	print *, "Iterations:", n
	print *, "Monte Carlo Estimation:", sums
	print *, "Actual value:", actual
	print *, "Relative, absolute error:", error
	print *, "Time:", time
end program MC
