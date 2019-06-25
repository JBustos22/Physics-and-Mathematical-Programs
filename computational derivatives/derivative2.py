#! /usr/bin/env python
"""
This program defines a function f(x) that returns the value of x*(x-1) 
and a function der(f,x) that returns the derivative of a function f 
at a value x with a delta of 10e-2 through 10e-18 by a step-size of 
1e-2. The der function is then used to find the derivatives to different
approximations at x=1

Jorge Bustos
Feb 22, 2019
"""
from __future__ import division, print_function
import numpy as np


def f(x):
	return x*(x-1)
	
def der(f,x):
	d = 10e-2 #delta
	for i in range(0,9,1): #will use six values
		print("d = ",d,":","f'(1)= ",(f(x+d)-f(x))/d)
		d = d*1.0e-2 #d will change 6 times by a factor of 1e-2
		
der(f,1)