#! /usr/bin/env python
"""
This program reads the file "n3pi.dat" containing event data for 
a photon beam incident on a proton target. The program creates
Lorentz vectors using the TLorentzVector class and finds the 
missing Lorentz vector for the neutron 

Jorge Bustos
PHZ4151C
Florida State University
April 22, 2019
Exercise 10 Part 2
"""

from __future__ import division, print_function
import numpy as np
import ROOT
#
Beam = ROOT.TLorentzVector()
PiPlus = [ROOT.TLorentzVector(),ROOT.TLorentzVector()]
PiMinus = ROOT.TLorentzVector()
Target = ROOT.TLorentzVector(0, 0, 0, 0.938)
nEvents = 0
nPiPlus = 0
#
with open("n3pi.dat", "r") as dataFile:
	# open file and read in ascii events line-by-line
	# the line will contain either the number of particles which indicates start of an event
	# or the line contains particle information: id charge Px Py Pz E
	# 
	for line in dataFile:
		word = line.split() # split line into a list of words
		value = int(word[0])
		if value == 4:
			if nEvents <= 5 and nEvents > 0:
				print("The Neutron mass for event #",nEvents,"is: ", Neutron.Mag()*1000,"MeV/c^2")
			nPiPlus = 0
			nEvents += 1
		elif value == 1  :
			# photon beam
			Beam.SetPxPyPzE( float(word[2]), float(word[3]), float(word[4]), float(word[5]) )
		elif value == 8  :
			# piPlus meson
			PiPlus[nPiPlus].SetPxPyPzE( float(word[2]), float(word[3]), float(word[4]), float(word[5]) )
			nPiPlus += 1	
		elif value == 9  :
			# piMinus meson
			PiMinus.SetPxPyPzE( float(word[2]), float(word[3]), float(word[4]), float(word[5]) )
		
		#missing neutron vector
		Neutron = Beam + Target - (PiPlus[0] + PiPlus[1] + PiMinus)

			


# Done reading all events from data file
print("\nTotal events read:", nEvents)