#!/usr/bin/python

import sys
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

def gcirc(racat, deccat, rapnt, decpnt):
	ra = str(racat)
	dec = str(deccat)
	pra = str(rapnt)
	pdec = str(decpnt)

	print('Arc Distance from Pointing: ') # prints gcirc

	c1 = SkyCoord(ra, dec, frame='icrs')
	c2 = SkyCoord(pra, pdec, frame='icrs')
	sep = c1.separation(c2)
	sep = sep.arcminute

	#print ra
	#print dec
	#print pra
	#print pdec
	#print sep
	
	if sep < 30.1:
    	    print sep
	else:
    	    print(">30")
