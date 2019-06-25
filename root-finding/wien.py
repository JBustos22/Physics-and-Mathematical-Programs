#! /usr/bin/env python
"""
This program uses the binary search to find the solution
to a non-linear equation relating to Wien's displacement 
constant. Through the solution, Wien's constant is found 
and used to find the surface temperature of the Sun.

Jorge Bustos
Mar 26, 2019
"""

from __future__ import division, print_function
import numpy as np
import scipy.constants as spc

def f(x):
	return 5*np.e**(-1*x) + x - 5
	
xa,xb = 0.0,0.0
for x in np.arange(0,10,1):
	if f(x) < 0:
		xa = x
	elif f(x) > 0:
		xb = x
	if (xa != 0 and xb != 0):
		break

xm = (xa+xb)/2
e = 10e-6
while np.absolute(xa-xb) > e:
	if f(xm)*f(xa) > 0:
		xa = xm
	else:
		xb = xm
	xm = (xa+xb)/2
	
b = np.absolute(spc.h*spc.c/(spc.Boltzmann*xm))
print("Wien's displacement constant is: ",b,"m*K")

wl_sun = 502e-9
T_sun = b/wl_sun
print("The surface temperature of the Sun is:",T_sun,"K")