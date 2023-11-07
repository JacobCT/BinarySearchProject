#!/usr/bin/python

import sys
import numpy as np
from astropy import units as u
from astropy.coordinates import SkyCoord

ra = str(sys.argv[1])
dec = str(sys.argv[2])
pra = str(sys.argv[3])
pdec = str(sys.argv[4])

print sys.argv[0] # prints gcric

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
    print ""
