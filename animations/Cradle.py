"""
This program simulates Newton's Cradle. Tow balls of equal radius are simulated and animated
to show harmonic motion with energy and momentum conservation. Two smaller balls are placed 
on top of them to show the pivot for each pendulum.

Jorge Bustos
Feb 17, 2019
"""
from __future__ import division, print_function
import vpython as vp
import numpy as np

#initializing  the constants
vp.canvas(width=400,height=600)
l=500 #radius of harmonic motion
r=l/10 #radius of the spheres, one tenth of it
g=9.81
theta_0 = 0.5 #initial angle of pendulum in radians

#pivots

pivot1 = vp.sphere(pos=vp.vector(-1*r,0,0), radius=10, color=vp.color.white)
pivot2 = vp.sphere(pos=vp.vector(r,0,0), radius=10, color=vp.color.white)

#pendulums

p1 = vp.sphere(pos=vp.vector(-1*r,-1*l,0), radius=r, color=vp.color.yellow)
p2 = vp.sphere(pos=vp.vector(0,-1*l,0), radius=r, color=vp.color.cyan)


for t in np.arange(0,10000,0.01): #harmonic motion
    vp.rate(500)
    theta=theta_0*np.cos(np.sqrt(g/l)*t)
    x = l*np.sin(theta)
    y = -1*l*np.cos(theta)
    if theta <= 0: #if statements are used to stop the motion of one pendulum and begin the motion
        p1.pos = vp.vector(x-r,y,0) #of the other one to simulate the transfer of energy and momentum.
    if theta >= 0:
        p2.pos = vp.vector(x+r,y,0)
