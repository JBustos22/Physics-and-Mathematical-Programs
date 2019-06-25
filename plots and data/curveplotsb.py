#! /usr/bin/env python
"""
This program uses matplotlib to plot the Galilean spiral function

Jorge Bustos
Feb 12, 2019
"""
from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np
import math as m

size = 1000
theta = np.linspace(0,24*m.pi,size)
r = theta**2
x = r*np.cos(theta)
y = r*np.sin(theta)

plt.plot(x,y)
plt.title("Spiral Function")
plt.savefig("Spiral.png")
plt.show()