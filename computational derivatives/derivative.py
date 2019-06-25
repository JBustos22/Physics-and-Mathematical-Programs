#! /usr/bin/env python
"""
This program defines a function f(x) that returns the value of x*(x-1) 
and a function der(f,x,d) that returns the derivative of a function f 
at a value x with a delta of d. It uses the limit definition of a derivative.
The program then uses the derivative function to find the derivative of f(x)
at x=4 with a delta of 0.1

Jorge Bustos
Feb 22, 2019
"""
from __future__ import division, print_function
import numpy as np

def f(x):
	return x*(x-1)
	
def der(f,x,d):
	return (f(x+d)-f(x))/d #approximation of derivative formula

print(2*1 - 1) #analytical derivative of f(x) at x = 1
print(der(f,1,10e-2)) #prints derivative of f(x) at x = 1 and delta = 10e-2