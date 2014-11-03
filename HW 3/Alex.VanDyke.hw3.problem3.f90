program find_primes
    implicit none
	! Variable declaration
	real :: t1, t2
    integer :: n, num, div, i

	! Start clock
	call cpu_time(t1)


	
	! Query the user for an input value for maximum number, N
	print *, "What is the range value (n)?"

	! If the value is less than or equal to 2, send error
	do
		read *, n
	    if (n >= 2) EXIT
    	print *, "N must be >= 2, please try again: "
	end do

    i = 1
	! 2 will always be included, print it and count it as the first prime
    print *, "Prime number #", i, ": 2"

	! Check all other primes from 3 to n
    do num = 3, n, 2
		div = 3

		! Check for divisibility and that divisor**2 is less than n
		! because max number needed for checking is sqrt(n)
		do
	   		if (div*div > num .OR. mod(num, div) == 0) exit
	    	div = div + 2
		end do
		
		! If prime, add to the counter and print the prime number
		if (div*div > num) then
	    	i = i + 1
	    	print *, num
		end if
    end do

	call cpu_time(t2)

	! Print the total number of primes in the range
	print *, "There are",i, "primes in the range of 2 to", n

	print *, "Time = ", t2-t1," seconds."
	
end program find_primes




