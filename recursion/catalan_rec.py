#! /usr/bin/env python
from __future__ import division, print_function

# Made by: Jorge Bustos
# This program calculates the nth Catalan number by using a recursive function.
# he function is defined such that it calls itself.

def catalan(n):
	if n==0:
		return 1 #case n=0
	elif n>0:
		return catalan(n-1)*(4*n - 2)/(n+1) #case otherwise
	else:
		return 0 #invalid

n = float(raw_input("Enter a value of n: "))

print("The Catalan number",int(n),"is:", int(catalan(n)))