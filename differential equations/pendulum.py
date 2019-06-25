#! /usr/bin/env python
"""
This program uses the Runge-Kutta method to solve
the nonlinear pendulum ODEs. The runge-kutte function
takes in two dimensions, one for each of the 1st order
ODEs derived from the main equation.

Jorge Bustos
April 12, 2019
"""

from __future__ import division, print_function
import matplotlib.pyplot as plt
import numpy as np
import sys


def runge_kutta4(func, r, t, h):
    """ 
	4th order Runge-Kutta method for ODEs
    """
    k1 = h*func(r, t)
    k2 = h*func(r+0.5*k1, t+0.5*h)
    k3 = h*func(r+0.5*k2, t+0.5*h)
    k4 = h*func(r+k3, t+h)
    return (k1 + 2*k2 + 2*k3 + k4)/6
   



def pendulum(r, t):
    g,L = 9.8,.1 #constants
    theta = r[0]
    omega = r[1]
    return np.array([omega, (-g/L)*np.sin(theta)], float)

#initialiton
nSteps = 1000
nArgs = len(sys.argv)
theta_0 = 5 #defaults to 5
if 1 < nArgs < 3 :
    # get initial angle from command line
    theta_0 = int(sys.argv[1])
elif nArgs > 1:
    print("\nBad command line input\n")
    sys.exit("Usage: "+sys.argv[0]+" <theta_0>"+"\n")


tMin,tMax = 0.0,20.0
tStep = (tMax-tMin)/nSteps

tPoints = np.arange(tMin, tMax, tStep)
thetaPoints,omegaPoints = [],[]

theta0,omega0 = theta_0,0.0
r = np.array([theta0,omega0], float)


for t in tPoints:
    thetaPoints += [r[0]]
    omegaPoints += [r[1]]
    r += runge_kutta4(pendulum, r, t, tStep)
	
plt.plot(tPoints,thetaPoints)
plt.xlabel("time")
plt.ylabel("theta")
plt.title("Nonlinear Pendulum angle with the vertical vs time")
plt.show()

plt.plot(thetaPoints, omegaPoints)
plt.xlabel("theta")
plt.ylabel("angular velocity")
plt.title("Nonlinear Pendulum phase space")
plt.show()
