#! /usr/bin/env python
"""
This program finds the greatest possible number such that when added to 1.0, the 
output is still 1.0. They are found for float16, float32, float64, and float128.

Jorge Bustos
Feb 22, 2019
"""
from __future__ import division, print_function
import numpy as np

#float16

e16 = np.float16(4.8e-4) #computer accuracy epsilon
x16 = np.float16(1.0) + e16
print("float 16: ",x16)

#float32

e32 = np.float32(5.9e-8)
x32 = np.float32(1.0) + e32
print("float 32: ",x32)

#float64

e64 = np.float64(1.1e-16)
x64 = np.float64(1.0) + e64
print("float 64: ",x64)

#float128

e128 = np.float128(5.4e-20)
x128 = np.float128(1.0) + e128
print("float 128: ",x128)
