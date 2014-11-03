!Numerical solver for temperature across a 1D surface using multiple boundary conditions, constant k, and constant Qdot

module TempSolver
	implicit none
	!Variable declaration
	double precision, dimension(1:6,1:6) :: A, D, Id
	double precision, dimension(1:6) :: x, b, x_new, Temp
	double precision :: Heat, dx, L, aa, bb, E, F, G, H
	integer :: i, j, n
contains

subroutine TempSolve(k, Qdot, T0, dTdx_0, TL, dTdx_L, BCs)

	!Take in the function values
	double precision, intent(in) :: k, Qdot, T0, dTdx_0, TL, dTdx_L
	integer, intent(in) :: BCs
	
	!Dirilicht conditions
	if ( BCs .eq. 0 ) then
		E = 1.0
		F = 0.0
		G = 1.0
		H = 0.0
	!Left side boundary conditions
	else if ( BCs .eq. 1 ) then
		E = 1.0
		F = 1.0
		G = 0.0
		H = 0.0
	!Right side boundary conditions
	else if ( BCs .eq. 2 ) then
		E = 0.0
		F = 0.0
		G = 1.0
		H = 1.0
	end if

	!Define the boundary condition equations
	aa = E*T0 + F*dTdx_0
	bb = G*TL + H*dTdx_L		
	
	n = 6
	L = 5

	dx = L/(n-1)
	Heat = -Qdot*(dx**2.0)/k
	
	!Create the middle 4 rows of the coefficient matrix of Ax = b
	!Also create the middle 4 rows of the idendity and diagonal matrices
	do i=2, n-1
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

	!Create the first and last row of the ID, Diag, and Coeff matrices
	do j=1, n
		A(1,j) = 0
		D(1,j) = 0
		Id(1,j) = 0
		A(n,j) = 0
		D(n,j) = 0
		Id(n,j) = 0
	end do

	!Use the equations to define the boundary conditions
	A(1,1) = E
	A(1,2) = F
	A(6,5) = H
	A(6,6) = G
	b(1) = aa
	b(6) = bb
	D(1,1) = 1
	D(6,6) = 1
	Id(1,1) = 1
	Id(6,6) = 1

	!Create the x vector to solve for
	do i=1,n
		x(i) = 1
	end do
	
	x_new = 0.0*x
	
	!Invert the diagonal matrix
	call inverse(D, D, 6)
	
	!Loop through to get a relative distance of current to previous of 0.0001
	do while (maxval(abs(x_new - x)) .gt. 0.0001)
		x = x_new
		x_new = matmul((Id-matmul(D, A)),x) + matmul(D,b)
	end do 
	Temp = x_new
	print *, Temp
	
end subroutine TempSolve

!Found online
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
double precision a(n,n), c(n,n)
double precision L(n,n), U(n,n), b(n), d(n), x(n)
double precision coeff
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
end module TempSolver
	
	
	
	
	
	
	
