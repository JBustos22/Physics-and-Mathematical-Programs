#! /usr/bin/env python
from __future__ import division, print_function
import math as m

"""
This program calculates and prints the height of a satellite given the orbit period

Jorge Bustos
"""
G,M,R = 6.67e-11,5.97e24,6371e3

T = float(raw_input("Enter the period T of the satellite's orbit (in seconds): "))

height = ((G*M*(T**2))/(4*m.pi**2))**(1/3) - R

print("The height at which the satellite is orbiting is",height,"meters")
