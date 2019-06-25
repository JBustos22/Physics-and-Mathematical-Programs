#! /usr/bin/env python
"""
This program uses the numpy.random module and an algorithm to generate
random numbers and plot them to create the Barnsley fern fractal

Jorge Bustos
Mar 5, 2019
"""
from __future__ import division, print_function
import numpy as np
import math as m
import matplotlib.pyplot as plt

N = 10000
x,y = 0.5,0.0
plt.scatter(x,y,c="b",s=1)

for k in np.arange(0,N):
	r = np.random.random() #random number in the range [0.0,1.0)
	if r < 0.02:
		x_new,y_new = 0.5,y*0.27
	elif (r >= 0.02) and (r <= 0.17):
		x_new,y_new = -0.139*x + 0.263*y + 0.57, 0.246*x +0.224*y-0.036
	elif (r > 0.17) and (r <= 0.3):
		x_new,y_new = 0.17*x - 0.215*y + 0.408, 0.222*x + 0.176*y + 0.0893
	elif (r > 0.3) and (r < 1):
		x_new,y_new = 0.781*x + 0.034*y + 0.1075, -0.032*x + 0.739*y + 0.27
	plt.scatter(x_new,y_new,c="b",s=1)
	x,y = x_new,y_new
		
# plt.xlim(0.2, 0.6) #zooming to show fractal pattern
# plt.ylim(0.2, 0.6)
plt.show()

