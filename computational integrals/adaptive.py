#! /usr/bin/env python
"""
This program uses the numint module's adaptive trapezoidal and
adaptive simpson functions to calculate the integral of a functions
it compares the accuracy of the two.

Jorge Bustos
Mar 4, 2019
"""
from __future__ import division, print_function
import numint as ni
import numpy as np

def g(x):
	return (np.sin(np.sqrt(100*x)))**2
	
print("\nUsing adaptive trapezoidal method: \n")

ni.atrapezoidal(g,0,1,0.000010)

print("\nUsing adaptive simpson's method: \n")

ni.asimpson(g,0,1,0.000010)