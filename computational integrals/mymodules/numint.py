#! /usr/bin/env python
"""
This is the numerical integration module that is used in other programs.
It includes: trapezoidal and simpson's method, their adaptive versions, and 
a generalized n-dimensional monte carlo integration function.

Jorge Bustos
Mar 4, 2019
"""
from __future__ import division, print_function
import sys
import numpy as np

	
def trapezoidal(f,a,b,N=1000):
	h = (b-a)/N
	s = 0.5*(f(a)+f(b))
	for k in range(1,N+1):
		s += f(a+k*h)
	return(h*s)

def simpson(f,a,b,N=1000):	
	h = (b-a)/N #width of intervals
	s = (f(a) + f(b)) #the two lone terms inside the parentheses
	for k in range(1,int(N/2+1)): #first summation term
		s += 4*f(a+(2*k-1)*h)
	for j in range(1,int(N/2)): #second summation term
		s += 2*f(a+2*j*h)
	return 1/3*h*s #multiplying what's outside
	
def atrapezoidal(f,a,b,e):
	N = 1
	e2 = e + 1
	while (e2 >= e):
		I1 = trapezoidal(f,a,b,N)
		N = 2*N
		I2 = trapezoidal(f,a,b,N)
		e2 = (1/3)*(I2-I1)
		if e2 < 0:
			e2 = e2 * -1
		print("N: ",N)
		print("Integral estimate: ",I2)
		print("Error of integral: ",e2)
	return N
	
def asimpson(f,a,b,e):
	N = 1
	e2 = e + 1
	while (e2 >= e):
		I1 = simpson(f,a,b,N)
		N = 2*N
		I2 = simpson(f,a,b,N)
		e2 = (1/15)*(I2-I1)
		if e2 < 0:
			e2 = e2 * -1
		print("N: ",N)
		print("Integral estimate: ",I2)
		print("Error of integral: ",e2)
	return N
		
def montecarlo(f, dim, limit, N=100):
	I = 1/N
	sum = 0
	for k in range(dim):
		I *= (limit[k][1] - limit[k][0])
	for i in np.arange(N):
		x = []
		for n in range(dim):
			x += [limit[n][0] + (limit[n][1] - limit[n][0])*np.random.random()]
		if dim < 3:
			for n in range(3-dim):
				x += [0]
		sum += f(x)
	return I*sum
	
def f(x):
	return 1
def g(x):
	return x[0]**2 + x[1]**2 + x[2]**2
tdim = 3
tlimit = [[0,1],[0,1],[0,1]]

def test_functions():
    """
    Routines to test module functions.  To execute test of function run 
    module as python program along with commandline argument "test"
        example: "mypython test" 
    """

    if(trapezoidal(f,0,1,1000) > 1.0) and (trapezoidal(f,0,1,1000) < 1.1):
        print("Trapezoidal function is good")
    else:
        print("WARNING!!!\n trapezoidal() function failed test\n DO NOT USE!!!")
		
    if(simpson(f,0,1,1000) == 1.0 ):
        print("Simpson function is good")
    else:
        print("WARNING!!!\n simpson() function failed test\n DO NOT USE!!!")
    if(atrapezoidal(f,0,1,.001) == 512):
        print("Adaptive trapezoidal function is Good")
    else:
        print("WARNING!!!\n atrapezoidal() function failed test\n DO NOT USE!!!")
		
    if(asimpson(f,0,1,.001) == 4):
        print("Adaptive simpson function is good")
    else:
        print("WARNING!!!\n asimpson() function failed test\n DO NOT USE!!!")
		
    if(montecarlo(f,tdim,tlimit,1000) > 0) and (montecarlo(f,tdim,tlimit,1000) < 1.5):
        print("Monte Carlo function is good")
    else:
        print("WARNING!!!\n montecarlo() function failed test\n DO NOT USE!!!")
		

	
# main
#

if __name__ == '__main__':
    # the test block
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_functions()



