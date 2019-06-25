#! /usr/bin/env python
"""
This program uses the secat menthod to find the value of 
the distance from the center of the Earth to the first
lagrange point, L1, where a satellite will orbit the Earth
in perfect synchrony with the Moon.

Jorge Bustos
Mar 26, 2019
"""

from __future__ import division, print_function
import numpy as np
import scipy.constants as spc
import sys

def f(r):
	M,R,m,w = 5.974e24, 3.844e8, 7.348e22, 2.662e-6
	return spc.G*M/(r**2) - spc.G*m/((R-r)**2) - (w**2)*r
	
def slope(y,r1,r2):
	return (y(r2)-y(r1))/(r2-r1)

target = 1e-10
ra = 6.371e6
rb = 7.0e6

while np.abs(ra-rb) > target:
	r = rb - f(rb) / slope(f,ra,rb)
	ra,rb = rb, r

print("The first lagrange point is located at :",r/1e3,"km from the center of the Earth")