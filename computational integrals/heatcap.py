#! /usr/bin/env python
"""
This program uses the numint module's simpson function to
numerically calculate the heat capacity of a 1000 cubic
cm sample of Aluminum. A plot of heat capacity vs. temperature
is created.

Jorge Bustos
Mar 4, 2019
"""

from __future__ import division, print_function
import numint as ni
import numpy as np
import matplotlib.pyplot as plt

def C(T):
	V = .001
	kB = 1.38064852e-23
	p = 6.022e28
	Dt = 428
	a = 1e-11
	b = Dt/T
	def f(x):
		return (x**4 * np.e**x)/(np.e**x - 1)**2
	I = ni.simpson(f,a,b,50)
	return 9 * V * p * kB * (T/Dt)**3 * I
	
T = np.linspace(5,500,1000)
C = C(T)
plt.plot(T,C)
plt.xlabel("Temperature (K)")
plt.ylabel("Heat Capacity (J/K)")
plt.title("Heat Capacity of a Sample of Aluminum")
plt.savefig("heatcap.png")
plt.show()