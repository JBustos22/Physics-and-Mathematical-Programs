#! /usr/bin/env python
"""
This program finds the eigen-energies for a given potential.
It solves schrodinger's equation using the runge kutta 4th
order method. Then, the secant method of root-finding is used
to find the energies by applying the boundary condition that
eigenfunctions must go to zero for large x. The program also 
exploits symmetry and parity to find the initial conditions. 
Lastly, the program normalizes the eigenfunctions and finds
the expectation value of position and momentum.

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
	if x >= 1:
		dphi = 2*(np.abs(x)-E)*psi
	else:
		dphi = 2*(-1*E)*psi
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
xMin,xMax = 0,3.0
deltaX = (xMax-xMin)/nSteps
xValues = np.arange(xMin, xMax, deltaX)

parity = 'odd'

if parity == 'even':
	x0, psi0, phi0 = 0,1,0
else:
	x0, psi0, phi0 = 0,0,1
	
r = np.array([x0,psi0,phi0],float)

target = 1e-6
E1, E2 = 3.1,3.2
while np.abs(E1-E2) > target:
	psi = wavefunction(schrodinger, r, xValues, deltaX, E1)
	psi1 = psi[-1]
	psi = wavefunction(schrodinger, r, xValues, deltaX, E2)
	psi2 = psi[-1]
	E1,E2 = E2, E2 - psi2 * (E2 - E1)/(psi2-psi1)
	

psi_x = wavefunction(schrodinger, r, xValues, deltaX, E2)

#Extention to negative values
if parity == 'even':
	psi_x = np.append(psi[::-1],psi_x[1:])
else:
	psi_x = np.append(-psi[::-1],psi_x[1:])
xValues = np.append(-xValues[::-1],xValues[1:])

#Normalization
norm = 2*np.sqrt(psi_x.dot(psi_x) * deltaX)
psi_x = psi_x/norm

#Plotting
plt.scatter(xValues, psi_x, s = .5)
plt.xlabel("x")
plt.ylabel("psi(x)")
plt.show()

#Expectation values
x2_exp = psi_x.dot( xValues*xValues*psi_x) * deltaX

psi_p = np.zeros(len(xValues))
for i in range(len(xValues)):
	if np.abs(xValues[i]) >= 1:
		psi_p[i] = 2.0*(E2 - np.abs(xValues[i])) * psi_x[i]
	else:
		psi_p[i] = 2.0*(E2) * psi_x[i]

p2_exp = psi_x.dot(psi_p) * deltaX

#Final data
print("Energy Value: ", E2)
print("Normalization constant: ", norm)
print("<x^2>: ", x2_exp)
print("<p^2>: ", p2_exp)

