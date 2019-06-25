#! /usr/bin/env python
"""
This program plots a fractal pattern using matplotlib

Jorge Bustos
Feb 12, 2019
"""
from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np
import math as m

plt.scatter(-1,0,c="b",s=.1)
plt.scatter(0,m.sqrt(3),c="b",s=.1)
plt.scatter(1,0,c="b",s=10)
x = 0
y = 0
r = 0
iterations = 200000 #how many points to plot
for i in range (0,iterations,1):
	plt.scatter(-1*x,-1*y,c="b",s=.1)
	r = np.random.randint(3) #chooses a number from 0 to 2 randomly
	if r == 0: 		#for vertex (-1,0)
		x = (x + 1)/2
		y = (y - 0)/2
	elif r == 1: 	#for vertex (0,sqrt(3))
		x = (x - 0)/2
		y = (y - m.sqrt(3))/2	
	else:			#for vertex(1,0)
		x = (x - 1)/2
		y = (y - 0)/2		
plt.savefig("fractal.png")
plt.show()