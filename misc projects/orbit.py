#! /usr/bin/env python
from __future__ import division, print_function
import math as m

# This program asks the user for the distance and speed at perihelion of a celestial entity orbiting the Sun.
# With this data, it calculates and returns the distance and speed at aphelion, as well as the period and 
# eccentricity of the orbital motion
#Made by Jorge Bustos

G,M = 6.6738e-11,1.9891e30 #where G is the gravitational constant and M is the mass of the Sun

L1 = float(raw_input("Enter the distance from the Sun at perihelion (in meters): "))
v1 = float(raw_input("Enter the speed at perihelion (in meters per second): "))

#from here, I use b_ and c_ to simplify the quadratic formula for v2

b_ = 2*G*M/(v1*L1)
c_ = (2*G*M/L1)-v1**2
v2 = (b_ -m.sqrt(b_**2 - 4*c_))/2 #note that I didn't use -b_ because I ommited the negative in its calculation

L2 = L1*v1/v2

a = 0.5*(L1 + L2) #Semi-major axis, not to be confused with a_
b = m.sqrt(L1*L2) #Semi-minor axis,not to be confused with b_
T = (2*m.pi*a*b/(L1*v1))/3.154e7 #I convert the period to years for a more convenient display
e = (L1 - L2)/(L2+L1)

print("\nThe distance at aphelion is: ",L2," m\n")
print("\nThe speed at aphelion is: ",v2," m/s\n")
print("\nThe period of orbit is ",T," yr\n")
print("\nThe orbital eccentricity is: ",e,"\n")


