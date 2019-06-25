#! /usr/bin/env python
"""
This program uses virtual python to animate a Helium atom model. The red spheres are
protons, the blue spheres are neutrons, and the smaller green spheres are electrons.

Jorge Bustos
Feb 17, 2019
"""
from __future__ import division, print_function
import vpython as vp
import numpy as np

r_nuc= 1.3 #the radius of the nucleons
r_e = .4	#the radius of the electrons
r_o = 10	#the radis of the electrons' orbitals


proton1 = vp.sphere(pos=vp.vector(1,1,0),radius=r_nuc, color=vp.color.red)
proton2 = vp.sphere(pos=vp.vector(-1,-1,0),radius=r_nuc, color=vp.color.red)
neutron1 = vp.sphere(pos=vp.vector(1,-1,0),radius=r_nuc, color=vp.color.blue)
neutron2 = vp.sphere(pos=vp.vector(-1,1,0),radius=r_nuc, color=vp.color.blue)

e1 = vp.sphere(pos=vp.vector(r_o,0,0),radius=r_e, color=vp.color.green)
e2 = vp.sphere(pos=vp.vector(0,0,r_o),radius=r_e, color=vp.color.green)

for theta in np.arange(0,50*np.pi,.01): #circular motion
   vp.rate(50)
   e1.pos = vp.vector(r_o*np.cos(theta),r_o*np.sin(theta),0)
   e2.pos = vp.vector(r_o*np.cos(theta),0,r_o*np.sin(theta))
