#include <cmath>
#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <time.h>
using namespace std;

void MidPoint(double, double, int);
void MidPoint3(double, double, int);
void MidPoint10(double, double, int);
void MonteCarlo(double, double, int);
int i, j, k, l, m, n, o, p, q, r, s, dim, range;
double realintegral[3];
double a, b, x, f, error, sum=0.0, midpoint=0, mc=0;

int main() 
{
	//Get the lower and upper bounds from user
	int N[3] = {1, 3, 10};
	cout << "Enter lower bound: ";
	cin >> a;
	cout << "Enter upper bound: ";
	cin >> b;
	cout << endl;

	//Loop through Monte Carlo for dimensions 1, 3, & 10
	for (i=0; i<3; i++)
	{
		realintegral[i] = pow(2,N[i])/pow(3,N[i]);
		MonteCarlo(a, b, N[i]);
		cout<<endl;
	}
	//Midpoint methods for each dimension
	MidPoint(a, b, N[0]);
	MidPoint3(a, b, N[1]);
	MidPoint10(a, b, N[2]);
	cout << endl;
	
	cout << "real values are:";
	cout << "	" << realintegral[0] << " for 1 dimension";
	cout << "	" << realintegral[1] << " for 3 dimensions";
	cout << "	" << realintegral[2] << " for 10 dimensions" << endl;

	return 0;
}

void MidPoint(double a, double b, int dim)
{
	double xa, dx;
	n = 10;
	range = n/dim;
	dx = (b-a)/range;
	sum = 0.0;
	for (j=0; j<range; j++)	
	{
		xa = dx*j + dx/2;
		f = sqrt(xa)*dx;
		sum = sum + f;
	}

	error = abs(1-sum/realintegral[0]);
	cout << dim << " Dimensional Midpoint Method" << endl;
	cout << "Midpoint estimation: " << sum << endl;
	cout << "Actual value: " << realintegral[0] << endl;
	cout << "Rel, abs error: " << error << endl;
	cout << endl;
}

void MidPoint3(double a, double b, int dim)
{
	double xa, xb, xc, dx;
	n = 10;
	range = n/dim;
	dx = (b-a)/range;
	sum = 0.0;
	for (j=0; j<range; j++)	
	{
		xa = dx*j + dx/2;
		for (k=0; k<range; k++)
		{
			xb = dx*k + dx/2;
			for (l=0; l<range; l++)
			{
				xc = dx*l + dx/2;
				f = sqrt(xa*xb*xc)*pow(dx,dim);
				sum = sum + f;
			}
		}
	}

	error = abs(1-sum/realintegral[1]);
	cout << dim << " Dimensional Midpoint Method" << endl;
	cout << "Midpoint estimation: " << sum << endl;
	cout << "Actual value: " << realintegral[1] << endl;
	cout << "Rel, abs error: " << error << endl;
	cout << endl;
}

void MidPoint10(double a, double b, int dim)
{
	double xa, xb, xc, xd, xe, xf, xg, xh, xi, xj, dx;
	n = 10;
	range = n/dim;
	dx = (b-a)/range;
	sum = 0.0;
	for (j=0; j<range; j++)	
	{
		xa = dx*j + dx/2;
		for (k=0; k<range; k++)
		{
			xb = dx*k + dx/2;
			for (l=0; l<range; l++)
			{
				xc = dx*l + dx/2;
				for (m=0; m<range; m++)
				{
					xd = dx*m + dx/2;
					for (n=0; n<range; n++)
					{
						xe = dx*n + dx/2;
						for (o=0; o<range; o++)
						{
							xf = dx*o + dx/2;
							for (p=0; p<range; p++)
							{
								xg = dx*p + dx/2;
								for (q=0; q<range; q++)
								{
									xh = dx*q + dx/2;
									for (r=0; r<range; r++)
									{
										xi = dx*r + dx/2;
										for (s=0; s<range; s++)
										{
											xj = dx*s + dx/2;
											f = sqrt(xa*xb*xc*xd*xe*xf*xg*xh*xi*xj)*pow(dx,dim);
											sum = sum + f;
										}
									}
								}
							}
						}
					}
				}
			}
		}
	}

	error = abs(1-sum/realintegral[2]);
	cout << dim << " Dimensional Midpoint Method" << endl;
	cout << "Midpoint estimation: " << sum << endl;
	cout << "Actual value: " << realintegral[2] << endl;
	cout << "Rel, abs error: " << error << endl;
	cout << endl;
}

void MonteCarlo(double a, double b,int dim)
{
	double timer, t1, t2;
	t1 = time(NULL);
	n = 100000;
	sum = 0.0;
	
	//Loop through the histories
	for (j=0; j<n; j++)
	{
		x = 1.0;

		//Calculate x1*x2*...*xn for given dimension
		for (k=0; k<dim; k++)
		{
			x = x*(a+(b-a)*(float)rand()/RAND_MAX);
		}
		
		//function is sqrt(x1*x2*...*xn)
		f = sqrt(x);

		//add all calculations up and divide by histories (MC Quadrature)
		sum += f/n;
	}

	error = abs(1-sum/realintegral[i]);
	t2 = time(NULL);
	timer = difftime(t2, t1);
	cout << "Monte Carlo Method" << endl;
	cout << "Dimension: " << dim << endl;
	cout << "Monte Carlo estimation: " << sum << endl;
	cout << "Actual value: " << realintegral[i] << endl;
	cout << "Rel, abs error: " << error << endl;
	cout << "Time: " << timer << endl;
}





