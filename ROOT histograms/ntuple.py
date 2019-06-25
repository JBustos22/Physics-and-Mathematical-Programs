#! /usr/bin/env python
"""
DumpData.py is a program which read in a simple ascii data file 
containing particle physics event Four-Vector information.  The program
prints the particle energies for the event and then print out a total event count.

Paul Eugenio
PHZ4151C
Florida State University
April 2, 2019

"""

from __future__ import division, print_function
import numpy as np
from ROOT import TLorentzVector, TNtuple, TCanvas, TFile

rootFile = TFile("ntp.root","RECREATE")

def f(x):
	return x**2

squares = TNtuple("sqntuple", "Squares", "x:x2")
sqCanvas = TCanvas("cc","squares", 10, 10, 800, 600)
sqCanvas.Divide(1,2)

for k in range(1,10,1):
	squares.Fill(k,f(k))

squares.Draw("x")
sqCanvas.cd(2)
squares.Draw("x2")

rootFile.Write()