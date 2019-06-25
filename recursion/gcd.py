#! /usr/bin/env python
from __future__ import division, print_function

# Made by: Jorge Bustos
# This program defines and uses a function that calculates the greatest common divisor.
#It prompts the user for two integers and returns their gcd.

def g(m,n):
	if n == 0:
		return m
	else:
		return g(n,m%n) 
		
n = float(raw_input("Enter a value of n: "))
m = float(raw_input("Enter a value of m: "))

print("The greatest common divisor of",int(n),"and",int(m),"is: ", int(g(n,m)))