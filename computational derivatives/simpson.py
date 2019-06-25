#! /usr/bin/env python
"""
This program uses the simpson method of approximating integrals to find
the integral of x**4-2*x+1 from 0 to 2.

Jorge Bustos
Feb 22, 2019
"""
from __future__ import division, print_function
import numpy as np

def f(x):
	return x**4 - 2*x + 1
	
N = 1000 #max value in summation
a = 0.0
b = 2.0
h = (b-a)/N #width of intervals
s = (f(a) + f(b)) #the two lone terms inside the parentheses
for k in range(1,int(N/2+1)): #first summation term
	s += 4*f(a+(2*k-1)*h)
for j in range(1,int(N/2)): #second summation term
	s += 2*f(a+2*j*h)
print(1/3*h*s) #multiplying what's outside
