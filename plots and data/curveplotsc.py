#! /usr/bin/env python
"""
This program uses matplotlib to plot Fay's butterfly function

Jorge Bustos
Feb 12, 2019
"""
from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np
import math as m

size = 1000 #for the amount of values between 0 and 2pi
theta = np.linspace(0,24*m.pi,size) #creates an array of theta values
r = np.e**(np.sin(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**5 #calculates the r for each theta value
x = r*np.cos(theta) #conversions to cartesian
y = r*np.sin(theta)

plt.plot(x,y)
plt.title("Fay's function")
plt.savefig("butterfly.png")
plt.show()

