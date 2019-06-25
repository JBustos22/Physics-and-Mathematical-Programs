#! /usr/bin/env python
"""
This program uses the numerical monte carlo integration function
from the numint module. It calculates the volume of an unit sphere
for dimensions 0, through 12, and creates a plot of hypervolume vs
dimension.

Jorge Bustos
Mar 4, 2019
"""

from __future__ import division, print_function
import numint as ni
import numpy as np
#import matplotlib.pyplot as plt

def f(x):
	return x[0]**2 + x[1]**2 + x[2]**2

N = 100
dim = 10
limit = []
print(0)
d = np.linspace(0,12,13)
I = [0]
for k in range(1,13,1):
	dim = k
	limit += [[0,1]]
	I +=[ni.montecarlo(f,dim,limit,N)]
	print(I[k])

# plt.plot(d,I)
# plt.xlabel("Dimension")
# plt.ylabel("Hypervolume")
# plt.title("Hypervolumes of an Unit Sphere vs. Dimension")
# plt.savefig("hyperspheres.png")
# plt.show()

