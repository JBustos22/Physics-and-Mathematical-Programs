#! /usr/bin/env python
"""
This program creates a class Vector3D that inherits the
class Vector2D. Additional functions are defined in the
Vector3D class. Some of these functions are used in the 
main program to create two 3-d vectors in order for the
dot product, cross product, addition and subtraction 
to be printed to the screen.

Jorge Bustos
April 5, 2019
"""
from __future__ import division, print_function
import numpy as np

class Vector2D:
	""" Vector2D Object declaration """
	def __init__(self, aX=0.0, aY=0.0):
		self.__x = aX
		self.__y = aY
	def x(self):
		return self.__x
	def y(self) :
		return self.__x
	def r(self) :
		return np.sqrt(self.x()**2 + self.y()**2)
	def __add__(self, other):
		""" ** """
		return Vector2D(self.x() + other.x(), self.y() + other.y())
	def __mul__(self, other):
		""" ** """
		return np.sqrt( self.x() * other.x() + self.y() * other.y() )
	def print(self):
		""" ** """
		print("vector(x,y) is (", self.x(), ",", self.y(),")")



class Vector3D(Vector2D):
	def __init__(self, aX, aY, aZ):
		Vector2D.__init__(self, aX, aY)
		self.__z = aZ
	def z(self):
		return self.__z
	def __add__(self, other):
		return Vector3D(self.x() + other.x(), self.y() + other.y(), self.z() + other.z())
	def mag(self):
		return self.x()**2 + self.y()**2 + self.z()**2
	def r(self):
		return np.sqrt(self.x()**2 + self.y()**2 + self.z()**2)
	def cos_theta(self):
		return np.arccos(self.z()/(self.x()**2 + self.y()**2))
	def phi(self):
		return np.arctan2(self.x(),self.y())
	def	__sub__(self, other):
		return Vector3D(self.x() - other.x(), self.y() - other.y(), self.z() - other.z())
	def __mul__(self, other):
		return np.sqrt( self.x() * other.x() + self.y() * other.y() + self.z() * other.z())
	def __truediv__(self, other):
		return Vector3D(self.y() * other.z() - self.z() * other.y(), self.z() * other.x() - self.x() * other.z(), self.x() * other.y() - self.y() * other.x())
	def print(self):
		print("vector(x,y) is (", self.x(), ",", self.y(),",", self.z(), "," , self.cos_theta(), ",", self.phi(),")")
		
#main 

V1 = Vector3D(2.0,3.0,4.0)
print("Vector 1:")
V1.print()

V2 = Vector3D(3.0,4.0,5.0)
print("Vector 2:")
V2.print()

print("The dot product of the two vectors is: ",V1 * V2)

V3 = V1 + V2
print("The vector resulting from their addition: ")
V3.print()

V4 = V2 - V1
print("The vector resulting from their subtraction: ")
V4.print()

V6 = V1 / V2
print("The vector resulting from their cross product: ")
V6.print()



