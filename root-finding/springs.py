#! /usr/bin/env python
"""
This program defines four functions corresponding to
the Bisection approach, False position approact, Secant
approach, and Newton's method approach to solving a 
non-linear equation. These functions are used to find the
proper root of the equilibrium equation for a mass suspended
via two springs.

Jorge Bustos
Mar 26, 2019
"""

from __future__ import division, print_function
import numpy as np
import scipy.constants as spc

def f(theta):
	m,L_0,k,g = 5,0.3,1000,9.81
	return np.tan(theta) - np.sin(theta) - (m*g)/(2*k*L_0)
def dfdx(theta):
	return (1/np.cos(theta))**2 - np.cos(theta)

def Bisection(f,xa,xb,e):
	xm = (xa+xb)/2
	i = 0
	while np.absolute(xa-xb) > e:
		i += 1
		if f(xm)*f(xa) > 0:
			xa = xm
		else:
			xb = xm
		xm = (xa+xb)/2
	r = [xm,i]
	return r

print(Bisection(f,25,30,1e-10))

def FalsePos(f,xa,xb,e):
	def m(x1,x2):
		return (f(x2)-f(x1))/(x2-x1)
	def b(x1,x2):
		return f(x1)- m(x1,x2)*(x1)
		
	xz = -1*b(xa,xb)/m(xa,xb)
	i = 0
	
	while np.abs(xa-xb) > e:
		i+=1
		if f(xz) == 0:
			break
		elif f(xz)*f(xa) > 0:
			xa = xz
		else:
			xb = xz
		xz = -1*b(xa,xb)/m(xa,xb)
	r = [xz, i]
	return r
print(FalsePos(f,27,29,1e-6))

def Secant(f,xa,xb,e):
	def slope(y,x1,x2):
		return (y(x2)-y(x1))/(x2-x1)
	i = 0
	while np.abs(xa-xb) > e:
		i+=1
		x = xb - f(xb) / slope(f,xa,xb)
		xa,xb = xb, x
	r = [x,i]
	return r
	
print(Secant(f,28,30,1e-10))

def Newton(f,dfdx,x,xL,e):
	i = 0
	while np.abs(x-xL) > e:
		i+=1
		xL = x
		x = xL- f(xL)/dfdx(xL)
	r = [x,i]
	return r
	
print(Newton(f,dfdx,27,28,1e-10))
		