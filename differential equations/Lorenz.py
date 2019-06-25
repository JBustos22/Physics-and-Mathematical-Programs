#! /usr/bin/env python
"""
This program uses the Runge-Kutta method to solve
the Lorenz equations. The Lorenz equations model 
seemingly chaotic weather phenomena. Using the 4th 
order Runge-Kutta method, the three equations are 
solved and a plot of y vs t and x vs z is created.
The first plot shows the chaotic nature of the motion,
and the second shows the famous "Strange Attractor".

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
	

def lorenz(r,t): #Definition of 3 ODES
	sigma, r_const, b = 10.0, 28.0, 8/3 #setting constants
	x,y,z = r[0],r[1],r[2]
	return np.array([sigma*(y-x), (r_const*x)-y-(x*z), (x*y)-(b*z)],float)

nSteps = 1000
tMin,tMax = 0.0,50.0
tStep = (tMax-tMin)/nSteps
tPoints = np.arange(tMin, tMax, tStep)

#Initial conditions
xPoints,yPoints,zPoints = [],[],[]
x0,v0,z0 = 0.0,1.0,0.0
r = np.array([x0,v0,z0], float)

for t in tPoints:
	xPoints += [r[0]]
	yPoints += [r[1]]
	zPoints += [r[2]]
	r += runge_kutta4(lorenz,r,t,tStep)
	
plt.plot(tPoints,yPoints)
plt.xlabel("time")
plt.ylabel("y")
plt.title("y component of Lorenz equation vs. time")
plt.show()

plt.plot(xPoints,zPoints)
plt.xlabel("x")
plt.ylabel("z")
plt.title("The Strange Attractor")
plt.show()