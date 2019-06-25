#! /usr/bin/env python
"""
This program reads the file "n3pi.dat" containing event data for 
a photon beam incident on a proton target. The program creates
Lorentz vectors using the TLorentzVector class and finds the 
missing Lorentz vector for the neutron. Then, it uses the Ntuple
class to fill and Ntuple object with all the lorentz vectors for every
event and generates it on a 2x4 Canvas

Jorge Bustos
PHZ4151C
Florida State University
April 22, 2019
Exercise 10 Part 3
"""

from __future__ import division, print_function
import numpy as np
from ROOT import TLorentzVector, TNtuple, TCanvas, TFile, TBrowser
#
Beam = TLorentzVector()
PiPlus = [TLorentzVector(),TLorentzVector()]
PiMinus = TLorentzVector()
Target = TLorentzVector(0, 0, 0, 0.938)
nEvents = 0
nPiPlus = 0


IMspectra = TNtuple("imntuple", "Invariant Mass Spectra", "npip1pip2pim:pip1pip2pim:pip1pim:pip2pim:pip1pip2:npip1:npip2:npim")

with open("n3pi.dat", "r") as dataFile:
	# open file and read in ascii events line-by-line
	# the line will contain either the number of particles which indicates start of an event
	# or the line contains particle information: id charge Px Py Pz E
	#

	rootFile = TFile("imNtp.root","RECREATE")
	
	for line in dataFile:
		word = line.split() # split line into a list of words
		value = int(word[0])
		if value == 4:	
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
		
		if value == 8 and nPiPlus == 2:
			Neutron = Beam + Target - (PiPlus[0] + PiPlus[1] + PiMinus) #missing neutron vector
			n,pip1,pip2,pim = Neutron.Mag(), PiPlus[0].Mag(), PiPlus[1].Mag(),PiMinus.Mag()
			im1, im2, im3, im4, im5, im6, im7, im8 = n+pip1+pip2+pim, pip1+pip2+pim, pip1+pim, pip2+pim, pip1+pip2, n+pip1, n+pip2, n+pim
			IMspectra.Fill( im1, im2, im3, im4, im5, im6, im7, im8 ) #filling Ntuple
			


rootFile.Write() #saving the Ntuple in a root file

IMCanvas = TCanvas("cc","Invariant mass spectra", 10, 10, 1000, 700) #creating a 2x4 canvas
IMCanvas.Divide(2,4)

IMCanvas.cd(1) #Navigation and filling of Canvas
IMspectra.Draw("npip1pip2pim")
IMCanvas.cd(2)
IMspectra.Draw("pip1pip2pim")
IMCanvas.cd(3)
IMspectra.Draw("pip1pim")
IMCanvas.cd(4)
IMspectra.Draw("pip2pim")
IMCanvas.cd(5)
IMspectra.Draw("pip1pip2")
IMCanvas.cd(6)
IMspectra.Draw("npip1")
IMCanvas.cd(7)
IMspectra.Draw("npip2")
IMCanvas.cd(8)
IMspectra.Draw("npim")

end_statement = raw_input("Press any key to exit the program...")