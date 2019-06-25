#! /usr/bin/env python
"""
This program creates a density plot of the surface of Silicon

Jorge Bustos
Feb 12, 2019
"""
from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np
import math as m

data = np.loadtxt("stm.txt",float)
plt.imshow(data,origin="lower")
plt.title("Density plot of Silicon's surface")
plt.savefig("Silicon.png")
plt.show()
