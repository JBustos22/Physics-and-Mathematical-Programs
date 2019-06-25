#! /usr/bin/env python
"""
This program uses the Runge-Kutta method to solve
the Duffing oscillator equation of motion. The main
equation (2nd order) is reduced to two 1st order ODEs
which are defined in the program and applied the Runge-
Kutta method to. It also plots points of v and x in the 
Poincare Section.

Jorge Bustos
April 12, 2019
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(f, r, t, h): #Runge Kutta Definition
	"""
	4th order Runge-Kutta method for ODEs
	"""
	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1,t+0.5*h)
	k3 = h*f(r+0.5*k2,t+0.5*h)
	k4 = h*f(r+k3,t+h)
	return (k1 + 2*k2 + 2*k3 + k4)/6

def duffing(r,t):
	B,b = 7,0.01 #constants
	return np.array([r[1],B*np.cos(t)-r[0]**3-b*r[1]],float) #returns [x,v]

tMin,tMax = 0.0,250.0
tStep = (2*np.pi)/360

#Initialization
xPoints,vPoints,tPoints = [],[],[]
x0,v0 = 3.0,0.0
r = np.array([x0,v0], float)
count = 0

for t in np.arange(tMin, tMax, tStep):
	if count % 360 == 0:
		xPoints += [r[0]]
		vPoints += [r[1]]
		tPoints += [t]
	r += runge_kutta4(duffing,r,t,tStep)
	count += 1

plt.plot(xPoints,vPoints)
plt.xlabel("x")
plt.ylabel("v")
plt.title("Poincare Section of the Duffing Oscillator")
plt.show()