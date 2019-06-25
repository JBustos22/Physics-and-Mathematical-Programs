#! /usr/bin/env python
"""
This program uses the random aspect of the numpy module
to simulate two die being thrown at random, a fraction of 
double sixes to throws is calculated and compared to the 
expected value of 1/36.

Jorge Bustos
Mar 4, 2019
"""

from __future__ import division, print_function
import numint as ni
import numpy as np


N = 1e6
counter = 0
for i in np.arange(0,N,1):
	d1 = np.random.randint(1,7)
	d2 = np.random.randint(1,7)
	if (counter == 0):
		print(d1,d2)
	if (d1 == 6) and (d2 == 6):
		counter +=1
frac = counter/N
print("\tSummary: \n")
print("Number of double sixes: ",counter)
print("Number of dice throws: ",N)
print("Double six fraction: ",frac)
