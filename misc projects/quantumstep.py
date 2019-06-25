#! /usr/bin/env python
"""
This program calculates and prints out the transmission and reflection
probabilities of a particle with mass m and energy E, encountering a 
potential step V.

Jorge Bustos
Mar 5, 2019
"""
from __future__ import division, print_function
import numpy as np

h_bar = 6.582119514e-16
m = 9.11e-31
E = 10 * 1.6021766208e-19
V = 9 * 1.6021766208e-19

k1 = np.sqrt(2*m*E)/h_bar
k2 = np.sqrt(2*m*(E-V))/h_bar

T = 4*k1*k2/(k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print("The transmission probability is: ",T)
print("The reflection probability is: ",R)