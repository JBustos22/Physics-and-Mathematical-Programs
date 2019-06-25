#! /usr/bin/env python
"""
This program defines the Hermite polynomial function and uses it to calculate
the first few wavefunctions of the quantum harmonic oscillator and plot them.
Then, the room-mean-squared (RMS) is calculated from 0 to max_n, which is inputted
by the user.

Jorge Bustos
Mar 5, 2019
"""
from __future__ import division, print_function
import numpy as np
import math as m
import matplotlib.pyplot as plt

def trapezoidal(f,a,b,n,N=1000):
	h = (b-a)/N
	s = 0.5*(f(a,n)+f(b,n))
	for k in range(1,N+1):
		s += f(a+k*h,n)
	return(h*s)

def H(x,n):
	if n >= 0:
		if n == 0:
			return 1
		elif n == 1:
			return 2*x
		else:
			return 2*x*H(x,n-1)-2*(n-1)*H(x,n-2) #recursive part
	else:
		return 0


x = np.linspace(-5,5,10000)
for n in range(0,4):
	plt.scatter(x,(1/(np.sqrt((2**n)*np.math.factorial(n)*np.sqrt(np.pi))))*np.e**((-1*x**2)/2)*H(x,n),s = 0.5)

plt.show()

n = 3
x2 = np.linspace(-10,10,1000)
y2 = (1/(np.sqrt(2**n*np.math.factorial(n)*np.sqrt(np.pi))))*np.e**(-1*x2**2/2)*H(x2,n)
plt.scatter(x2,y2,s=0.5)
plt.show()

MAX_N = int(raw_input("Enter an integer for maximum N for which to calculate the RMS: "))
def f(x,n):
	return x**2 * ((1/(np.sqrt(2**n*np.math.factorial(n)*np.sqrt(np.pi))))*np.e**(-1*x**2/2)*H(x,n))**2 #definition of integrand
print("\t\tRMS")
for n in range(0,MAX_N+1):
	print("n = ",n,"\t",np.sqrt(trapezoidal(f,-100,100,n,100))) #the integral is square rooted to get RMS