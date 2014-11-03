program MidPoint
	implicit none
	!Variable declaration
	integer :: iter=100, dims=10, i, j, k, l, m, n, o, p, q, r, ranges
	real :: xa, xb, xc, xd, xe, xf, xg, xh, xi, xj
	real :: dx, f, actual, a, b, error
	integer :: t1, t2, clock_rate, clock_max, time
	double precision :: sums = 0.0

	CALL system_clock(t1, clock_rate, clock_max)

	!Calculate the actual value
	actual = 2.0**dims/3.0**dims

	!Get upper and lower bounds from user
	print *, "Enter lower bound: "
	read *, a 
	print *, "Enter upper bound: "
	read *, b
	
	!Set the number of midpoits per dimension
	ranges = iter/dims
	
	!Midpoint rule for 10 dimensions
	dx = (b-a)/ranges
	do i=0, ranges-1
		xa = dx*i + dx/2
		do j=0, ranges-1
		xb = dx*j + dx/2
			do k=0, ranges-1
				xc = dx*k + dx/2
				do l=0, ranges-1
					xd = dx*l + dx/2
					do m=0, ranges-1
						xe = dx*m + dx/2
						do n=0, ranges-1
							xf = dx*n + dx/2
							do o=0, ranges-1
								xg = dx*o + dx/2
								do p=0, ranges-1
									xh = dx*p + dx/2
									do q=0, ranges-1
										xi = dx*q + dx/2
										do r=0, ranges-1
											xj = dx*r + dx/2 
											f = sqrt(xa*xb*xc*xd*xe*xf*xg*xh*xi*xj)*(dx**dims)
											sums = sums + f
										end do
									end do
								end do
							end do
						end do
					end do
				end do
			end do
		end do
	end do

	error = abs(1-sums/actual)
	CALL system_clock(t2, clock_rate, clock_max)
	time = t2 - t1
print *, "Midpoint approximation:", sums
print *, "Actual value:", actual
print *, "Relative, absolute error:", error
print *, "Time: ", time
end program MidPoint	
