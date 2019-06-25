#! /usr/bin/env python
"""
This program utilizes visual python to simulate Newton's Cradle, similar to Cradle.py, it takes
realism more seriously by introducing damping. A damping constant is prompted for the user to type,
and it will apply it to the harmonic motion of the pendulums.

Jorge Bustos
Feb 17, 2019
"""
from __future__ import division, print_function
import vpython as vp
import numpy as np

vp.canvas(width=400,height=600)
l=500
r=l/10
g=9.81
theta_0_initial = 0.5 #initial placement of pendulum in radians
mu = float(raw_input("Please enter the desired damping constant: ")) #asks user for damping constant

#pivots

o1 = vp.sphere(pos=vp.vector(-1*r,0,0), radius=10, color=vp.color.white)
o2 = vp.sphere(pos=vp.vector(r,0,0), radius=10, color=vp.color.white)

#pendulums

e1 = vp.sphere(pos=vp.vector(-1*r,-1*l,0), radius=r, color=vp.color.yellow)
e2 = vp.sphere(pos=vp.vector(0,-1*l,0), radius=r, color=vp.color.cyan)


for t in np.arange(0,10000,0.01):
    vp.rate(1000)
    theta_0 = theta_0_initial*np.e**(-1*mu*t) #damping affects theta_0
    theta=theta_0*np.cos(np.sqrt(g/l)*t) #new, non--variable theta_0
    x = l*np.sin(theta)
    y = -1*l*np.cos(theta)
    if theta <= 0:
        e1.pos = vp.vector(x-r,y,0)
    if theta >= 0:
        e2.pos = vp.vector(x+r,y,0)