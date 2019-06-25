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

class Vector2D:
	""" Vector2D Object declaration """
	def __init__(self, aX=0.0, aY=0.0):
		self.setR(np.sqrt(aX**2 + aY**2))
		self.setTheta( np.arctan2(aY, aX) )
	def setR(self, aR):
		self.__r = aR
	def setTheta(self, aTheta):
		self.__theta = aTheta
	def x(self):
		return self.r() * np.cos( self.theta() )
	def y(self) :
		return self.r() * np.sin( self.theta() )
	def r(self) :
		return self.__r
	def theta(self) :
		return self.__theta
	def __add__(self, other):
		""" ** """
		return Vector2D(self.x() + other.x(), self.y() + other.y())		
	def __mul__(self, other):
		""" ** """
		return sqrt( self.x() * other.x() + self.y() * other.y() ) 
	def print(self):
		""" ** """
		print("vector(x,y) is (", self.x(), ",", self.y(),")") 


#main
P1 = Vector2D()
P2 = Vector2D(1.0,1.0)
P3 = Vector2D(2.0,2.0)
P1.print()
P2.print()
P3.print()
P1 = P2 + P3
P1.print()
