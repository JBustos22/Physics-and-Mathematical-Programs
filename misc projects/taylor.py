#! /usr/bin/env python
"""
This program approximates the exponential functions through the use of 
a Taylor series sum function S(x,N) which takes in the value of x to calculate
and the number of terms - 1 N in the Taylor series. 

Jorge Bustos
Mar 5, 2019
"""
from __future__ import division, print_function
import numpy as np
import math as m

def S(x,N): #summation function
	s = 1
	for k in np.arange(1,N+1):
		s += (x**k)/np.math.factorial(k)
	return s

x = float(raw_input("Enter a value of x for which to estimate the exponential: " ))

if (x >= 0):
	print("The exponential function at the point ",x,"is approximately: ",S(x,50))
else:
	print("The exponential function at the point ",x,"is approximately: ",1/S(-1*x,50))	#for case of negatives
print("The exponential function at the point ",x,"is actually: ",m.exp(x))

