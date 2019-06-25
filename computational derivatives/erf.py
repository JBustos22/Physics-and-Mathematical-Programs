#! /usr/bin/env python
"""
This program uses the trapezoid method to approximate the Gaussian Error Function.
It computes E(3) and then plots the error function on a certain interval.

Jorge Bustos
Feb 22, 2019
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

def f(t):
	return np.e**(-1*t**(2))

def E(x):
	N = 100
	a = 0.0
	b = x
	h = (b-a)/N #width of intervals
	s = 0.5*(f(a) + f(b)) #the two lone terms inside the parentheses
	for k in range(1,int(N+1)):
		s += f(a+k*h)
	return h*s #multiplying by h outside

print(E(3))

x = np.linspace(-20,20,1000) #x values between -20 and 20, step 1000
y = E(x)
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("E(x)")
plt.title("Gaussian Error Function")
plt.savefig("erf.png")
plt.show()
