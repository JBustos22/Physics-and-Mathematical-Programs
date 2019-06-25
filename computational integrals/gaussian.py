#! /usr/bin/env python
"""
This program uses the simpson function of the numint module to 
numerically find the integral of the Guassian function from negative
infinity to positive infinity via a change of variable. The results is 
then compared to the expected value of sqrt(pi).

Jorge Bustos
Mar 4, 2019
"""

from __future__ import division, print_function
import numint as ni
import numpy as np

def gauss(z):
	return 1/(1-z)**2*np.e**(-1*((z/(1-z))**2))
a,b = 0,1-1e-15

print("Gaussian integral: ",2*ni.simpson(gauss,a,b,10000))

print("Square root of pi: ",np.sqrt(np.pi))
