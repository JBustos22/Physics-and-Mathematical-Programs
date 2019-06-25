#! /usr/bin/env python
"""
solarsystem.py uses virtual python to animate a model of our solar system.
The program uses multipliers to fix the radius of the planets and sun, as well
as the speed of the orbits for convenience.

Jorge Bustos
Feb 17, 2019
"""

from __future__ import division, print_function
import vpython as vp
import numpy as np

c1 = 0.0029 #multiplier for the radius of the planets
c1_s = 0.00005 #multiplier for the radius of the Sun
c2 = 1000 #multiplier for time of the orbit animation

Sun = vp.sphere(pos=vp.vector(0,0,0),radius = c1_s*695500, color = vp.color.yellow)
Mercury = vp.sphere(pos=vp.vector(57.9,0,0),radius = c1*2440,color=vp.color.cyan)
Venus = vp.sphere(pos=vp.vector(108.2,0,0),radius = c1*6052,color=vp.color.magenta)
Earth = vp.sphere(pos=vp.vector(149.2,0,0),radius = c1*6371,color=vp.color.blue)
Mars = vp.sphere(pos=vp.vector(227.9,0,0),radius = c1*3386,color=vp.color.red)
Jupiter = vp.sphere(pos=vp.vector(778.5,0,0),radius = c1*69173,color=vp.color.orange)
Saturn = vp.sphere(pos=vp.vector(1433.4,0,0),radius = c1*57316, color=vp.color.white)


for theta in np.arange(0,50*np.pi,.01): #circular motion, will stop when the planets reach 50pi
   vp.rate(50) #for smooth animations
   Mercury.pos = vp.vector(57.9*np.cos(c2*theta/88),57.9*np.sin(c2*theta/88),0)
   Venus.pos = vp.vector(108.2*np.cos(c2*theta/224.7),108.2*np.sin(c2*theta/224.7),0)
   Earth.pos = vp.vector(149.2*np.cos(c2*theta/365.3),149.2*np.sin(c2*theta/365.3),0)
   Mars.pos = vp.vector(227.9*np.cos(c2*theta/687),227.9*np.sin(c2*theta/687),0)
   Jupiter.pos = vp.vector(778.5*np.cos(c2*theta/4331.6),778.5*np.sin(c2*theta/4331.6),0)
   Saturn.pos = vp.vector(1433.4*np.cos(c2*theta/10759.2),1433.4*np.sin(c2*theta/10759.2),0)
