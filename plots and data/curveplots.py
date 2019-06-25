#! /usr/bin/env python
from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np
import math as m

size = 1000
x = np.zeros(size)
y = np.zeros(size)

for i in range (0,size,1):
	theta = i*2*m.pi/size
	x[i] = 2*np.cos(theta) + np.cos(2*theta)
	y[i] = 2*np.sin(theta) - np.sin(2*theta)
	
plt.plot(x,y)
plt.show()
	