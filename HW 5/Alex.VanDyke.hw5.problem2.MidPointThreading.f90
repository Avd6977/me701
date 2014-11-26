program MidPoint

    use omp_lib

	implicit none
	!Variable declaration
	integer :: n=120000, dims=2, i, j, ranges
	double precision :: dx, sums, f, actual, a, b, error, sums_partial, xa, xb

	actual = 2.0**dims/3.0**dims

	a = 0.0
	b = 1.0
	sums = 0.0
	sums_partial = 0.0
	
	!Set dx
	ranges = n/dims
	dx = (b-a)/ranges

	!Calculate midpoint integral
	!$omp parallel private(sums_partial, j, xb, f) shared(i, xa, sums)
	!$omp do
	do i=0, ranges-1
		xa = dx*i + dx/2
		do j=0, ranges-1
		    xb = dx*j + dx/2
		    f = sqrt(xa*xb)*(dx**dims)
		    sums_partial = sums_partial + f
        end do
	end do
    !$omp end do

    !$omp critical
    sums = sums + sums_partial
    !$omp end critical
	!$omp end parallel
error = abs(1-sums/actual)

print *, "Midpoint approximation:", sums
print *, "Actual value:", actual
print *, "Relative, absolute error:", error
end program MidPoint	
