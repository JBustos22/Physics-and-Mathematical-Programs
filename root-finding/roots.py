#! /usr/bin/env python
"""
This program uses Newton's method to calculate the roots
of a polynomial which has been entered by the user. It asks
for a polynomial function, its derivative, and the plotting range.
It then plots it, and asks the user for a value. Once a value
is entered, the root closest to that value is evaluated.

Jorge Bustos
Mar 4, 2019
"""

from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt

def Newton(f,dfdx,x,xL,e): #function defining the Newton method
	while np.abs(x-xL) > e:
		xL = x
		x = xL- f(xL)/dfdx(xL)
	return x

fx=raw_input("Enter a Polynomial: ") #turns the polynomial inputs into usable functions
def f(x):
	return eval(fx)

dfx = raw_input("Enter its derivative: ")
def df(x):	
	return eval(dfx)

a = int(raw_input("Enter the lower bound of your interval: "))
b = int(raw_input("Enter the upper bound of your interval: "))

x = np.linspace(a,b,1000)
plt.plot(x,f(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

x_i = 0

def isFloat(s): #functions that checks if it's a float
    try: 
        float(s)
        return True
    except ValueError:
        return False

while x_i != "q" :
	x_i = raw_input("Enter the starting value for root finding (q for quit): ")
	if isFloat(x_i): #checking for float
		print("The root of your polynomial is: ",Newton(f,df,float(x_i),1e4,1e-10))
		plt.plot(x,f(x))
		plt.xlabel("x")
		plt.ylabel("f(x)")
		plt.show()
	elif(x_i != "q"): #anything other than q or float
		print("invalid entry")
	
print("Goodbye!")