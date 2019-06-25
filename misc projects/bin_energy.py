#! /usr/bin/env python
from __future__ import division, print_function
import math as m

# This program asks the user for the atomic number Z and mass number A of a desired atom. With this information, it 
# returns the binding energy and binding energy per nucleon in MeV by using the semi-empirical mass formula
# Made by Jorge Bustos

a1,a2,a3,a4 = 15.67,17.23,0.75,93.2

A = float(raw_input("Enter the mass number of the atom: "))

Z = float(raw_input("Enter the atomic number of the atom: "))


#if the quantity is even, then when modded by 2 it will be zero

if (((A-Z)%2 == 0) and ((Z%2) == 0)): #case where A-Z and Z are both even
	a5 = 12.0
elif (((A-Z)%2 != 0) and ((Z%2)!=0)): #case where A-Z and Z are both odd
	a5 = -12.0
else:
	a5 = 0 #otherwise
	
binding_energy = a1*A - a2*(A**(2/3)) - a3*Z**2/(A**(1/3)) - (a4*(A-2*Z)**2)/A + a5/A**(1/2)


print("\nThe binding energy of the atom is : ",binding_energy, "MeV\n")

print("\nThe binding energy per nucleon of the atom is : ",binding_energy/A,"MeV\n")