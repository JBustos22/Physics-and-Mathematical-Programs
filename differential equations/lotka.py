#! /usr/bin/env python
"""
This program uses the Runge-Kutta method to solve
the lota-volterra ODEs. The equations describe the 
population of rabbits and foxes as time goes on.
It uses the method for two dimensions, one for each
equation. The two populations are plotted on top of 
each other to see the clear relation between them.

Jorge Bustos
April 12, 2019
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(f, r, t, h):
	"""
	4th order Runge-Kutta method for ODEs
	"""
	k1 = h*f(r,t)
	k2 = h*f(r+0.5*k1,t+0.5*h)
	k3 = h*f(r+0.5*k2,t+0.5*h)
	k4 = h*f(r+k3,t+h)
	return (k1 + 2*k2 + 2*k3 + k4)/6
	

#main

def lotka_volterra(r,t):
	alpha,beta,gamma,delta = 1.0, 0.5, 0.5, 2.0 #setting constants
	x = r[0]
	y = r[1]
	return np.array([alpha*x-beta*x*y, gamma*x*y-delta*y],float)
	

nSteps = 1000
tMin,tMax = 0.0,30.0
tStep = (tMax-tMin)/nSteps
tPoints = np.arange(tMin, tMax, tStep)

#initial conditions

xPoints,yPoints = [],[]
x0,y0 = 2.0,2.0
r = np.array([x0,y0], float)

for t in tPoints:
	xPoints += [r[0]]
	yPoints += [r[1]]
	r += runge_kutta4(lotka_volterra,r,t,tStep)
	

plt.plot(tPoints, xPoints,'-b', label = 'rabbits')
plt.plot(tPoints, yPoints,'-r', label = 'foxes')
plt.xlabel("time")
plt.ylabel("population")
plt.title("Population of rabbits and foxes with time")
plt.legend(loc='upper left')
plt.show()