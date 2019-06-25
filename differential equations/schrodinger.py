#! /usr/bin/env python
"""
This program solves schrodinger's equation for the potential
function V(x) = x**2 via the utilization of the 4th order runge
kutta method. The main purpose of this is to estimate the value
for the energy of the eigenfunctions. It finds two energies that 
bracket the eigen-energy and plots it. Note: the wavefunctions
plotted are neither eigenfunctions nor normalized.

Jorge Bustos
April 25, 2019
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(f, r, h, E): #Runge Kutta Definition
	"""
	4th order Runge-Kutta method for ODEs
	"""
	k1 = h*f(r, E)
	k2 = h*f(r+0.5*k1, E)
	k3 = h*f(r+0.5*k2, E)
	k4 = h*f(r+k3, E)
	return (k1 + 2*k2 + 2*k3 + k4)/6

def schrodinger(r,E):
	x = r[0]
	psi = r[1]
	phi = r[2]
	dpsi = phi
	dphi = 2*(x**2-E)*psi
	return np.array([x,dpsi, dphi], float)

def wavefunction(f, State, xValues, deltaX, E):
	s = np.copy(State)
	psi = []
	for x in xValues:
		psi += [s[1]]
		s[0] = x
		s += runge_kutta4(schrodinger, s, deltaX, E)
	return np.array(psi,float)

#main
nSteps = 1000
xMin,xMax = 0,3
deltaX = (xMax-xMin)/nSteps
xValues = np.arange(xMin, xMax, deltaX)

x0, psi0, phi0 = 0,1,0 #even parity BCs
r = np.array([x0,psi0,phi0],float)

#E = float(raw_input("Enter a value for E for which to find the wavefunction: "))

plt.scatter(xValues, wavefunction(schrodinger, r, xValues, deltaX, 0.6), s = .5)
plt.scatter(xValues, wavefunction(schrodinger, r, xValues, deltaX, 0.709),s = .5)
plt.scatter(xValues, wavefunction(schrodinger, r, xValues, deltaX, 0.8), s = .5)
plt.scatter(-1*xValues, wavefunction(schrodinger, r, xValues, deltaX, 0.6), s = .5)
plt.scatter(-1*xValues, wavefunction(schrodinger, r, xValues, deltaX, 0.709),s = .5)
plt.scatter(-1*xValues, wavefunction(schrodinger, r, xValues, deltaX, 0.8), s = .5)
plt.show()
