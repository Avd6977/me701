!Numerical solver for temperature across a 1D surface using Dirilicht boundary conditions, constant k, and constant Qdot

program TempSolver
	implicit none
	!Variable declaration
	integer :: n=5, i, j
	real :: k, Qdot, T0, TL, Heat, dx, dTdx_0 = 0.0, dTdx_L = 0.0, L = 5
	real :: E = 1.0, F = 1.0, G = 1.0, H = 1.0, aa = 0.0, bb = 0.0
	!For E*To + F*dTdx_0 = a and G*TL + H*dTdx_L = b
	real, dimension(0:5,0:5) :: A, D, Id
	real, dimension(0:5) :: x, b, x_new

	!Get boundary conditions, Qdot, and k from the user
	print *, "Enter the thermal conductivity (assumed constant), k: "
	read *, k
	print *, "Enter the constant heat flux, Qdot: "	
	read *, Qdot
	print *, "Only 2 of the next 4 are allowed to be defined, both Ts, or one side"
	print *, "Enter the boundary temperature at x=0: "
	read *, T0
	print *, "Enter the boundary temperature at x=L: "
	read *, TL
	print *, "Enter dTdx at x=0: "
	read *, dTdx_0
	print *, "Enter dTdx at x=L: "
	read *, dTdx_L

	aa = E*T0 + F*dTdx_0
	bb = G*TL + H*dTdx_L

	dx = L/n
	Heat = -Qdot*(dx**2.0)/k
	
	do i=1, n-1
		b(i) = Heat
		D(i,i) = -2
		Id(i,i) = 1
		A(i,i) = -2
		do j=0, n
			if ( j .ne. i) then
				A(i,j) = 0
				Id(i,j) = 0
				D(i,j) = 0
				if ( j .eq. i-1 .or. j .eq. i+1 ) then
					A(i,j) = 1
				end if
			end if
		end do
	end do

	do j=0, n
		A(0,j) = 0
		D(0,j) = 0
		Id(0,j) = 0
		A(n,j) = 0
		D(n,j) = 0
		Id(n,j) = 0
	end do
	A(0,0) = E
	A(0,1) = F
	A(5,4) = G
	A(5,5) = H
	b(0) = aa
	b(5) = bb
	D(0,0) = 1
	D(5,5) = 1
	Id(0,0) = 1
	Id(5,5) = 1

	do i=0,n
		x(i) = 1
	end do
	
	x_new = 0.0*x
	
	call inverse(D, D, 6)
	
	do while (maxval(abs(x_new - x)) .gt. 0.0001)
		x = x_new
		x_new = matmul((Id-matmul(D, A)),x) + matmul(D,b)
	end do 
	print *, x_new
	
end program TempSolver


subroutine inverse(a,c,n)
!============================================================
! Inverse matrix
! Method: Based on Doolittle LU factorization for Ax=b
! Alex G. December 2009
!-----------------------------------------------------------
! input ...
! a(n,n) - array of coefficients for matrix A
! n      - dimension
! output ...
! c(n,n) - inverse matrix of A
! comments ...
! the original matrix a(n,n) will be destroyed 
! during the calculation
!===========================================================
implicit none 
integer n
real a(n,n), c(n,n)
real L(n,n), U(n,n), b(n), d(n), x(n)
real coeff
integer i, j, k

! step 0: initialization for matrices L and U and b
! Fortran 90/95 aloows such operations on matrices
L=0.0
U=0.0
b=0.0

! step 1: forward elimination
do k=1, n-1
   do i=k+1,n
      coeff=a(i,k)/a(k,k)
      L(i,k) = coeff
      do j=k+1,n
         a(i,j) = a(i,j)-coeff*a(k,j)
      end do
   end do
end do

! Step 2: prepare L and U matrices 
! L matrix is a matrix of the elimination coefficient
! + the diagonal elements are 1.0
do i=1,n
  L(i,i) = 1.0
end do
! U matrix is the upper triangular part of A
do j=1,n
  do i=1,j
    U(i,j) = a(i,j)
  end do
end do

! Step 3: compute columns of the inverse matrix C
do k=1,n
  b(k)=1.0
  d(1) = b(1)
! Step 3a: Solve Ld=b using the forward substitution
  do i=2,n
    d(i)=b(i)
    do j=1,i-1
      d(i) = d(i) - L(i,j)*d(j)
    end do
  end do
! Step 3b: Solve Ux=d using the back substitution
  x(n)=d(n)/U(n,n)
  do i = n-1,1,-1
    x(i) = d(i)
    do j=n,i+1,-1
      x(i)=x(i)-U(i,j)*x(j)
    end do
    x(i) = x(i)/u(i,i)
  end do
! Step 3c: fill the solutions x(n) into column k of C
  do i=1,n
    c(i,k) = x(i)
  end do
  b(k)=0.0
end do
end subroutine inverse
	
	
	
	
	
	
	
	
