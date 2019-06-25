#! /usr/bin/env python
"""
This program uses the Runge-Kutta method to solve
the Duffing oscillator equation of motion. The main
equation (2nd order) is reduced to two 1st order ODEs
which are defined in the program and applied the Runge-
Kutta method to. A plot of the position of the oscillator
with respect to time is created, as well as the phase 
space.

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

nSteps = 1000
tMin,tMax = 0.0,50.0
tStep = (tMax-tMin)/nSteps
tPoints = np.arange(tMin, tMax, tStep)

#Initialization
xPoints,vPoints = [],[]
x0,v0 = 3.0,0.0
r = np.array([x0,v0], float)

for t in tPoints:
	xPoints += [r[0]]
	vPoints += [r[1]]
	r += runge_kutta4(duffing,r,t,tStep)
	
plt.plot(tPoints,xPoints)
plt.xlabel("time")
plt.ylabel("x")
plt.title("Position of the Duffing Oscillator against time")
plt.show()

plt.plot(xPoints,vPoints)
plt.xlabel("x")
plt.ylabel("v")
plt.title("Phase space of the Duffing Oscillator")
plt.show()