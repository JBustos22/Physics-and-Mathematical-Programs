#! /usr/bin/env python
"""
This program uses matplotlib to plot the number of Sunspots per month
starting at January 1749.

Jorge Bustos
Feb 12, 2019
"""
from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("sunspots.txt",float)
x = data[0:1000,0] #reads only 1000 data points from 1st column
y = data[0:1000,1] # " 		" 		" 		"		" 2nd column

Y = np.zeros(len(y)) #creates an array full of zeros, of desired length
r = 5
for k in range(len(y)):
	if (k < r) or (k > 1000 - r): #for the case that the indices of y go out of bounds
		Y[k] = y[k]
	else:
		for m in range(k-r,k+r,1):
			Y[k] += 1/(2*r+1) * y[m]
			
plt.plot(x,y)
plt.plot(x,Y,"r") #plotting the running average as a red curve
plt.title("Sunspots by month since Jan 1749")
plt.xlabel("month")
plt.ylabel("Sunspots")
plt.savefig("Sunspots.png")
plt.show()